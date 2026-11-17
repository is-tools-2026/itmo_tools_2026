"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».

Запуск:
    python -m unittest -v test_coffee
"""

import os
import re
import subprocess
import sys
import unittest
from unittest import mock

import coffee
from coffee import (
    MENU,
    _is_int,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


# ============================================================
# _is_int (вспомогательная функция проверки целых чисел)
# ============================================================
class IsIntTestCase(unittest.TestCase):
    def test_positive_int(self):
        self.assertTrue(_is_int(5))

    def test_zero_and_negative_int(self):
        self.assertTrue(_is_int(0))
        self.assertTrue(_is_int(-3))

    def test_bool_is_not_int(self):
        self.assertFalse(_is_int(True))
        self.assertFalse(_is_int(False))

    def test_float_is_not_int(self):
        self.assertFalse(_is_int(2.0))

    def test_str_and_none_are_not_int(self):
        self.assertFalse(_is_int("5"))
        self.assertFalse(_is_int(None))


# ============================================================
# get_price
# ============================================================
class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_all_menu_items(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertEqual(get_price(name), price)

    def test_price_is_int(self):
        self.assertIsInstance(get_price("latte"), int)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_int_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_unhashable_name(self):
        # list нельзя искать в dict -> без проверки типа будет TypeError
        with self.assertRaises(ValueError):
            get_price(["latte"])

    def test_name_is_case_sensitive(self):
        with self.assertRaises(ValueError):
            get_price("Latte")

    def test_name_with_spaces(self):
        with self.assertRaises(ValueError):
            get_price(" espresso ")


# ============================================================
# calculate_order_total
# ============================================================
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_single_item(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(5, 0), 0)

    def test_big_numbers(self):
        self.assertEqual(calculate_order_total(10 ** 6, 280), 280_000_000)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 99.9), 299.7, places=2)

    def test_total_is_not_negative(self):
        self.assertTrue(calculate_order_total(2, 120) >= 0)

    def test_result_is_number_not_string(self):
        # calculate_order_total('latte', 5) без проверки вернёт строку 'lattelattelatte...'
        self.assertFalse(isinstance(calculate_order_total(2, 3), str))

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -280)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 5)

    def test_numeric_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("3", 280)

    def test_string_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(3, "280")

    def test_none_arguments(self):
        with self.assertRaises(ValueError):
            calculate_order_total(None, 280)
        with self.assertRaises(ValueError):
            calculate_order_total(3, None)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2.5, 280)

    def test_bool_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(True, 280)

    def test_nan_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, float("nan"))


# ============================================================
# get_most_expensive_drink
# ============================================================
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_result_for_default_menu(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_returns_tuple_of_two(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_name_is_in_menu(self):
        name, _ = get_most_expensive_drink()
        self.assertIn(name, MENU)

    def test_price_matches_menu(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(MENU[name], price)

    def test_price_is_maximum(self):
        _, price = get_most_expensive_drink()
        self.assertTrue(all(price >= other for other in MENU.values()))

    def test_not_the_cheapest(self):
        name, _ = get_most_expensive_drink()
        self.assertNotEqual(name, "tea")

    def test_custom_menu(self):
        with mock.patch.dict(coffee.MENU, {"a": 10, "b": 30, "c": 20}, clear=True):
            self.assertEqual(get_most_expensive_drink(), ("b", 30))

    def test_single_item_menu(self):
        with mock.patch.dict(coffee.MENU, {"only": 99}, clear=True):
            self.assertEqual(get_most_expensive_drink(), ("only", 99))


# ============================================================
# generate_wifi_password
# ============================================================
class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length_is_8(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_returns_string(self):
        self.assertIsInstance(generate_wifi_password(), str)

    def test_custom_lengths(self):
        for length in (8, 9, 12, 16, 64):
            with self.subTest(length=length):
                self.assertEqual(len(generate_wifi_password(length)), length)

    def test_only_latin_letters_and_digits(self):
        for _ in range(200):
            self.assertTrue(re.fullmatch(r"[A-Za-z0-9]+", generate_wifi_password()))

    def test_has_upper_lower_and_digit(self):
        # пароль случайный, поэтому проверяем много раз
        for _ in range(200):
            pwd = generate_wifi_password()
            with self.subTest(password=pwd):
                self.assertTrue(any(c.isupper() for c in pwd))
                self.assertTrue(any(c.islower() for c in pwd))
                self.assertTrue(any(c.isdigit() for c in pwd))

    def test_has_no_spaces(self):
        self.assertFalse(" " in generate_wifi_password())

    def test_passwords_are_different(self):
        passwords = {generate_wifi_password() for _ in range(20)}
        self.assertGreater(len(passwords), 1)

    def test_length_7_is_too_short(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-5)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")

    def test_float_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)

    def test_none_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(None)

    def test_bool_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(True)


# ============================================================
# format_receipt
# ============================================================
class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_returns_string(self):
        self.assertIsInstance(format_receipt("latte", 1), str)

    def test_receipt_full_format(self):
        receipt = format_receipt("latte", 3).strip()
        pattern = (
            r"Чек CampusCoffee\n"
            r"Напиток: latte\n"
            r"Количество: 3\n"
            r"Итого: 840 руб\."
        )
        self.assertRegex(receipt, pattern)

    def test_receipt_header(self):
        self.assertRegex(format_receipt("tea", 1), r"Чек CampusCoffee")

    def test_receipt_drink_line(self):
        self.assertRegex(format_receipt("espresso", 2), r"Напиток: espresso")

    def test_receipt_quantity_line(self):
        self.assertRegex(format_receipt("espresso", 2), r"Количество: 2")

    def test_receipt_total_line(self):
        self.assertRegex(format_receipt("espresso", 2), r"Итого: 300 руб\.")

    def test_receipt_total_is_integer(self):
        self.assertNotRegex(format_receipt("espresso", 2), r"Итого: \d+\.\d+")

    def test_receipt_zero_quantity(self):
        self.assertRegex(format_receipt("latte", 0), r"Итого: 0 руб\.")

    def test_receipt_all_menu_items(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertRegex(format_receipt(name, 2), rf"Итого: {price * 2} руб\.")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unhashable_name(self):
        with self.assertRaises(ValueError):
            format_receipt(["latte"], 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", None)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_bool_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", True)


# ============================================================
# Модуль целиком
# ============================================================
class ModuleTestCase(unittest.TestCase):
    def test_import_has_no_side_effects(self):
        """При импорте модуль не должен ничего печатать и не должен падать."""
        env = dict(os.environ, PYTHONIOENCODING="utf-8")
        result = subprocess.run(
            [sys.executable, "-c", "import coffee"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
