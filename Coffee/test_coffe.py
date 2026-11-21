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

    def test_normal_order(self):
        self.assertEqual(calculate_order_total(2, 150), 300)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_invalid_quantity_type(self):
        with self.assertRaises((TypeError, ValueError)):
            calculate_order_total("two", 150)

class MostExpensiveDrinkTestCase(unittest.TestCase):

    def test_most_expensive_drink(self):
        self.assertEqual(
            get_most_expensive_drink(),
            ("latte", 280)
        )

    def test_result_is_tuple(self):
        self.assertTrue(
            isinstance(get_most_expensive_drink(), tuple)
        )


class GenerateWifiPasswordTestCase(unittest.TestCase):

    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)

    def test_password_characters(self):
        password = generate_wifi_password()
        self.assertTrue(password.isalnum())
        self.assertTrue(password.isascii())

    def test_password_content(self):
        password = generate_wifi_password()
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(5)

    def test_invalid_length_type(self):
        with self.assertRaises((TypeError, ValueError)):
            generate_wifi_password("eight")


class FormatReceiptTestCase(unittest.TestCase):

    def test_normal_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_receipt_is_string(self):
        receipt = format_receipt("tea", 1)
        self.assertTrue(isinstance(receipt, str))

    def test_empty_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("cola", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -2)

    def test_invalid_quantity_type(self):
        with self.assertRaises((TypeError, ValueError)):
            format_receipt("latte", "two")

    def test_receipt_format(self):
        receipt = format_receipt("latte", 1)
        self.assertRegex(receipt, r"Чек Coffee")


if __name__ == "__main__":
    unittest.main()