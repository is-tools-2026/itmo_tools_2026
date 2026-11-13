"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)

# Пример
class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            get_price(5)
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_order_total(self):
        self.assertEqual(calculate_order_total(3, 280), 840)


class MostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(
            get_most_expensive_drink(),
            ("latte", 280)
        )


class WifiPasswordTestCase(unittest.TestCase):
    def test_default_password(self):
        password = generate_wifi_password()
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        self.assertEqual(len(password)) 
        self.assertFalse(any(c not in allowed for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)


class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_format(self):
        expected = (
            "Чек CampusCoffee\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб."
        )
        self.assertEqual(
            format_receipt("latte", 2).strip(),
            expected
        )

    def test_empty_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

class BoundaryCasesTestCase(unittest.TestCase):
    def test_order_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_order_zero_price(self):
        self.assertAlmostEqual(calculate_order_total(2, 0), 0)

    def test_order_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

    def test_order_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -280)

    def test_order_quantity_as_text(self):
        with self.assertRaises(ValueError):
            calculate_order_total("2", 280)

    def test_order_price_as_text(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, "280")

    def test_drink_name_as_list(self):
        with self.assertRaises(ValueError):
            get_price(["latte"])

    def test_password_length_as_text(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")

    def test_receipt_quantity_as_text(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")