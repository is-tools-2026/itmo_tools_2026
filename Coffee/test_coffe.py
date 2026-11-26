"""Unit-тесты для модуля кофейни (coffee.py).

Запуск:
    python -m unittest test_coffee.py -v
"""
import os
import string
import subprocess
import sys
import unittest
from unittest import mock

import coffee
from coffee import (
    MENU,
    calculate_order_total,
    format_receipt,
    generate_wifi_password,
    get_most_expensive_drink,
    get_price,
)


# ============================================================
# get_price (пример из задания + дополнительные случаи)
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

    def test_price_is_positive_int(self):
        for name in MENU:
            with self.subTest(drink=name):
                self.assertIsInstance(get_price(name), int)
                self.assertGreater(get_price(name), 0)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_number_instead_of_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_none_instead_of_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_unhashable_name(self):
        # список нельзя искать в словаре -> без проверки типа будет TypeError
        with self.assertRaises(ValueError):
            get_price(["latte"])

    def test_name_is_case_sensitive(self):
        with self.assertRaises(ValueError):
            get_price("LATTE")


# ============================================================
# calculate_order_total
# ============================================================
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_single_item(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_large_quantity(self):
        self.assertEqual(calculate_order_total(1000, 250), 250000)

    def test_float_price(self):
        # 3 * 99.9 в float даёт 299.70000000000005
        self.assertAlmostEqual(calculate_order_total(3, 99.9), 299.7)

    def test_result_is_int_for_int_input(self):
        self.assertIsInstance(calculate_order_total(2, 100), int)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(0, 100)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 100)

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, 0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -100)

    def test_string_quantity(self):
        # "3" * 100 == "3"*100 -> строка вместо числа
        with self.assertRaises(ValueError):
            calculate_order_total("3", 100)

    def test_string_price(self):
        # 3 * "latte" == "lattelattelatte"
        with self.assertRaises(ValueError):
            calculate_order_total(3, "latte")

    def test_none_arguments(self):
        with self.assertRaises(ValueError):
            calculate_order_total(None, 100)
        with self.assertRaises(ValueError):
            calculate_order_total(2, None)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2.5, 100)

    def test_bool_quantity(self):
        # True == 1, но это явно не количество напитков
        with self.assertRaises(ValueError):
            calculate_order_total(True, 100)

    def test_nan_and_inf_price(self):
        for bad in (float("nan"), float("inf")):
            with self.subTest(price=bad):
                with self.assertRaises(ValueError):
                    calculate_order_total(1, bad)


# ============================================================
# get_most_expensive_drink
# ============================================================
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_latte_is_most_expensive(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_returns_tuple_of_two(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_price_is_maximum(self):
        _, price = get_most_expensive_drink()
        self.assertEqual(price, max(MENU.values()))

    def test_no_drink_is_more_expensive(self):
        _, price = get_most_expensive_drink()
        self.assertTrue(all(p <= price for p in MENU.values()))

    def test_name_is_in_menu(self):
        name, price = get_most_expensive_drink()
        self.assertIn(name, MENU)
        self.assertEqual(MENU[name], price)

    def test_not_the_cheapest(self):
        name, _ = get_most_expensive_drink()
        self.assertNotEqual(name, "tea")

    def test_follows_changed_menu(self):
        # функция не должна быть «зашита» под текущее меню
        with mock.patch.dict(coffee.MENU, {"gold_coffee": 999}):
            self.assertEqual(get_most_expensive_drink(), ("gold_coffee", 999))


# ============================================================
# generate_wifi_password
# ============================================================
class GenerateWifiPasswordTestCase(unittest.TestCase):
    ATTEMPTS = 300  # пароль случайный -> проверяем много раз

    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        for length in (8, 9, 12, 32, 128):
            with self.subTest(length=length):
                self.assertEqual(len(generate_wifi_password(length)), length)

    def test_returns_str(self):
        self.assertIsInstance(generate_wifi_password(), str)

    def test_only_latin_letters_and_digits(self):
        for _ in range(self.ATTEMPTS):
            self.assertRegex(generate_wifi_password(), r"^[A-Za-z0-9]+$")

    def test_has_lowercase_uppercase_and_digit(self):
        for _ in range(self.ATTEMPTS):
            pwd = generate_wifi_password()
            self.assertTrue(any(c in string.ascii_lowercase for c in pwd), pwd)
            self.assertTrue(any(c in string.ascii_uppercase for c in pwd), pwd)
            self.assertTrue(any(c in string.digits for c in pwd), pwd)

    def test_requirements_hold_for_long_password(self):
        for _ in range(50):
            pwd = generate_wifi_password(64)
            self.assertRegex(pwd, r"[a-z]")
            self.assertRegex(pwd, r"[A-Z]")
            self.assertRegex(pwd, r"[0-9]")

    def test_passwords_are_random(self):
        self.assertNotEqual(generate_wifi_password(32), generate_wifi_password(32))

    def test_too_short(self):
        for length in (7, 3, 1):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_wifi_password(length)

    def test_zero_and_negative_length(self):
        for length in (0, -1, -100):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_wifi_password(length)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("10")

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
    def test_receipt_contents(self):
        receipt = format_receipt("latte", 2)
        self.assertRegex(receipt, r"Напиток: latte\b")
        self.assertRegex(receipt, r"Количество: 2\b")
        self.assertRegex(receipt, r"Итого: 560 руб\.")

    def test_receipt_has_title(self):
        self.assertIn("Чек", format_receipt("tea", 1))

    def test_receipt_total_format(self):
        # «Итого: <число> руб.» — целое число, без копеек и «.0»
        self.assertRegex(format_receipt("espresso", 3), r"Итого: \d+ руб\.")

    def test_receipt_is_str(self):
        self.assertIsInstance(format_receipt("tea", 1), str)

    def test_total_matches_menu_price(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertIn(f"Итого: {price * 4} руб.", format_receipt(name, 4))

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("borscht", 1)

    def test_unhashable_name(self):
        with self.assertRaises(ValueError):
            format_receipt(["latte"], 1)

    def test_number_name_message_is_about_type(self):
        # для 0 и [] сообщение должно говорить про тип, а не "пустое"
        for bad in (0, []):
            with self.subTest(name=bad):
                with self.assertRaisesRegex(ValueError, "строкой"):
                    format_receipt(bad, 1)

    def test_zero_quantity(self):
        # чек на 0 напитков на 0 рублей не имеет смысла
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", None)


# ============================================================
# Модуль целиком
# ============================================================
class ModuleTestCase(unittest.TestCase):
    def test_import_has_no_side_effects(self):
        # при импорте модуль не должен ничего печатать в stdout
        # отдельный процесс: не влияет на остальные тесты
        folder = os.path.dirname(os.path.abspath(__file__))
        result = subprocess.run(
            [sys.executable, "-c", "import coffee"],
            cwd=folder, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_menu_prices_are_positive(self):
        self.assertTrue(all(isinstance(p, int) and p > 0 for p in MENU.values()))

    def test_menu_is_not_empty(self):
        self.assertFalse(len(MENU) == 0)


if __name__ == "__main__":
    unittest.main()