"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».

Запуск:
    python -m unittest test_coffee.py -v
"""

import re
import unittest
from unittest.mock import patch

from coffee import (
    MENU,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


# ============================================================
# get_price (пример из задания)
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

    def test_prices_are_positive(self):
        for name in MENU:
            with self.subTest(drink=name):
                self.assertTrue(get_price(name) > 0)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_non_string_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_unhashable_name(self):
        # список нельзя искать в словаре: должен быть ValueError, а не TypeError
        with self.assertRaises(ValueError):
            get_price([])

    def test_wrong_case(self):
        with self.assertRaises(ValueError):
            get_price("Espresso")

    def test_name_with_spaces(self):
        with self.assertRaises(ValueError):
            get_price(" espresso ")


# ============================================================
# calculate_order_total
# ============================================================
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_one_drink(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_result_is_int(self):
        self.assertIsInstance(calculate_order_total(2, 100), int)

    def test_large_quantity(self):
        self.assertEqual(calculate_order_total(10 ** 6, 280), 280_000_000)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(3, 0), 0)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 99.99), 299.97, places=2)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_string_quantity(self):
        # "3" * 280 в Python не падает, а даёт строку из 280 троек
        with self.assertRaises(ValueError):
            calculate_order_total("3", 280)

    def test_drink_name_instead_of_number(self):
        # calculate_order_total('latte', 5) возвращает 'lattelattelattelattelatte'
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 5)

    def test_string_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, "150")

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(None, 150)

    def test_none_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, None)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(1.5, 100)

    def test_bool_quantity(self):
        # True == 1, но «количество напитков» не должно быть булевым
        with self.assertRaises(ValueError):
            calculate_order_total(True, 100)


# ============================================================
# get_most_expensive_drink
# ============================================================
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_returns_tuple_of_two(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_name_and_price(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_price_matches_menu(self):
        name, price = get_most_expensive_drink()
        self.assertIn(name, MENU)
        self.assertEqual(price, MENU[name])

    def test_price_is_maximum(self):
        _, price = get_most_expensive_drink()
        self.assertTrue(all(price >= p for p in MENU.values()))

    def test_not_the_cheapest(self):
        name, _ = get_most_expensive_drink()
        self.assertNotEqual(name, "tea")

    def test_uses_current_menu(self):
        with patch.dict(MENU, {"mega_coffee": 999}):
            self.assertEqual(get_most_expensive_drink(), ("mega_coffee", 999))


# ============================================================
# generate_wifi_password
# ============================================================
class GenerateWifiPasswordTestCase(unittest.TestCase):
    RUNS = 200  # пароль случайный, поэтому проверяем много раз

    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        for length in (8, 9, 12, 64):
            with self.subTest(length=length):
                self.assertEqual(len(generate_wifi_password(length)), length)

    def test_returns_string(self):
        self.assertIsInstance(generate_wifi_password(), str)

    def test_only_latin_letters_and_digits(self):
        for _ in range(self.RUNS):
            self.assertRegex(generate_wifi_password(), r"^[A-Za-z0-9]+$")

    def test_has_uppercase(self):
        for _ in range(self.RUNS):
            self.assertTrue(any(c.isupper() for c in generate_wifi_password()))

    def test_has_lowercase(self):
        for _ in range(self.RUNS):
            self.assertTrue(any(c.islower() for c in generate_wifi_password()))

    def test_has_digit(self):
        for _ in range(self.RUNS):
            self.assertTrue(any(c.isdigit() for c in generate_wifi_password()))

    def test_passwords_are_random(self):
        self.assertNotEqual(generate_wifi_password(32), generate_wifi_password(32))

    def test_length_below_minimum(self):
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
            generate_wifi_password("10")

    def test_float_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)

    def test_none_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(None)


# ============================================================
# format_receipt
# ============================================================
class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_is_string(self):
        self.assertIsInstance(format_receipt("latte", 1), str)

    def test_receipt_contains_data(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("latte", receipt)
        self.assertIn("2", receipt)
        self.assertIn("560", receipt)

    def test_receipt_format_regex(self):
        receipt = format_receipt("latte", 2)
        self.assertRegex(
            receipt,
            r"Напиток: latte\s+Количество: 2\s+Итого: 560 руб\.",
        )

    def test_receipt_total_espresso(self):
        self.assertIn("Итого: 450 руб.", format_receipt("espresso", 3))

    def test_receipt_header(self):
        # по документации первая строка чека: «Чек CampusCoffee»
        self.assertIn("Чек CampusCoffee", format_receipt("tea", 1))

    def test_receipt_lines_order(self):
        lines = [l for l in format_receipt("tea", 4).splitlines() if l.strip()]
        self.assertEqual(len(lines), 4)
        self.assertTrue(lines[1].startswith("Напиток:"))
        self.assertTrue(lines[2].startswith("Количество:"))
        self.assertTrue(lines[3].startswith("Итого:"))

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", format_receipt("tea", 0))

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("tea", -1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("borsch", 1)

    def test_non_string_name(self):
        with self.assertRaises(ValueError):
            format_receipt(5, 1)

    def test_unhashable_name(self):
        with self.assertRaises(ValueError):
            format_receipt([], 1)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("tea", "2")

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("tea", None)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_bool_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", True)


if __name__ == "__main__":
    unittest.main()
