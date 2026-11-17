
"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
)


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

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            get_price(5)


class OrderTotalTestCase(unittest.TestCase):
    def test_total(self):
        self.assertEqual(calculate_order_total(2, 150), 300)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            calculate_order_total("2", 150)


class MostExpensiveTestCase(unittest.TestCase):
    def test_name(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")

    def test_price(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(price, 280)

    def test_result_type(self):
        result = get_most_expensive_drink()
        self.assertTrue(isinstance(result, tuple))


class WifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_length_12(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)

    def test_uppercase(self):
        password = generate_wifi_password()
        self.assertTrue(any(c.isupper() for c in password))

    def test_lowercase(self):
        password = generate_wifi_password()
        self.assertTrue(any(c.islower() for c in password))

    def test_digit(self):
        password = generate_wifi_password()
        self.assertTrue(any(c.isdigit() for c in password))

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            generate_wifi_password("8")


class FormatReceiptTestCase(unittest.TestCase):
    def test_total(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_title(self):
        receipt = format_receipt("latte", 1)
        self.assertIn("Чек CampusCoffee", receipt)

    def test_quantity(self):
        receipt = format_receipt("tea", 3)
        self.assertIn("Количество: 3", receipt)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("cola", 2)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 2)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", "2")


if __name__ == "__main__":
    unittest.main()
