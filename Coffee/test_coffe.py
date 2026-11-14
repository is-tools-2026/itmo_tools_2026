"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
Запуск: python -m unittest test_coffe.py -v
"""

import re
import string
import unittest

from coffee import (
    MENU,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_all_menu_items(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertEqual(get_price(name), price)

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
        with self.assertRaises(ValueError):
            get_price([])

    def test_wrong_case(self):
        with self.assertRaises(ValueError):
            get_price("Latte")


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_one_item(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(5, 0), 0)

    def test_result_is_int(self):
        self.assertIsInstance(calculate_order_total(2, 100), int)

    def test_almost_equal(self):
        self.assertAlmostEqual(calculate_order_total(3, 280) / 3, 280)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -280)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 5)

    def test_string_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(5, "280")

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(1.5, 280)

    def test_none(self):
        with self.assertRaises(ValueError):
            calculate_order_total(None, 280)

    def test_bool(self):
        with self.assertRaises(ValueError):
            calculate_order_total(True, 280)


class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_name_and_price(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_returns_tuple(self):
        self.assertIsInstance(get_most_expensive_drink(), tuple)

    def test_price_is_max(self):
        _, price = get_most_expensive_drink()
        self.assertEqual(price, max(MENU.values()))

    def test_not_cheapest(self):
        name, _ = get_most_expensive_drink()
        self.assertNotEqual(name, "tea")

    def test_drink_in_menu(self):
        name, _ = get_most_expensive_drink()
        self.assertIn(name, MENU)


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(20)), 20)

    def test_only_latin_and_digits(self):
        allowed = set(string.ascii_letters + string.digits)
        for _ in range(100):
            self.assertTrue(set(generate_wifi_password()) <= allowed)

    def test_has_required_chars(self):
        for _ in range(100):
            pwd = generate_wifi_password(8)
            self.assertTrue(any(c.isupper() for c in pwd))
            self.assertTrue(any(c.islower() for c in pwd))
            self.assertTrue(any(c.isdigit() for c in pwd))

    def test_passwords_differ(self):
        self.assertNotEqual(generate_wifi_password(16), generate_wifi_password(16))

    def test_too_short(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_and_negative(self):
        for bad in (0, -5):
            with self.subTest(length=bad):
                with self.assertRaises(ValueError):
                    generate_wifi_password(bad)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")

    def test_none_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(None)

    def test_float_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)


class FormatReceiptTestCase(unittest.TestCase):
    def test_format_regex(self):
        receipt = format_receipt("latte", 2)
        pattern = (r"^\n---Чек Coffee---\nНапиток: latte\n"
                   r"Количество: 2\nИтого: 560 руб\.\n$")
        self.assertRegex(receipt, pattern)

    def test_total_value(self):
        self.assertIn("Итого: 150 руб.", format_receipt("espresso", 1))

    def test_contains_name_and_quantity(self):
        receipt = format_receipt("tea", 4)
        self.assertIn("Напиток: tea", receipt)
        self.assertIn("Количество: 4", receipt)
        self.assertIn("Итого: 480 руб.", receipt)

    def test_returns_str(self):
        self.assertIsInstance(format_receipt("tea", 1), str)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("margarita", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            format_receipt([], 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_no_total_in_error_case(self):
        self.assertFalse(re.search(r"Итого", "ошибка"))


if __name__ == "__main__":
    unittest.main()
