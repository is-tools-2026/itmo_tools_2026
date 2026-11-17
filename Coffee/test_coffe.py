"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest
import string

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

    def test_numeric_name(self):
        with self.assertRaises(ValueError):
           get_price(5)

class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_regular_order(self):
        self.assertEqual(calculate_order_total(4,150),600)

    def test_zero_quanrity(self):
        self.assertEqual(calculate_order_total(0,150),0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(4,0),0)

    def test_negative_quanrity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1,150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2,-150)
            
    def test_fractional_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(1.5, 150)

    def test_boolean_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(True, 150)

class GetMostExpensiveDrinkTests(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(),("latte",280))

class GenerateWifiPasswordTests(unittest.TestCase):
    def test_default_lenght(self):
        self.assertEqual(len(generate_wifi_password()),8)

    def test_custom_lenght(self):
        self.assertEqual(len(generate_wifi_password(12)),12)

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_allowed_characters(self):
        password = generate_wifi_password()
        allowed = string.ascii_letters + string.digits
        self.assertTrue(all(char in allowed for char in password))

    def test_has_uppercase(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.isupper() for char in password))

    def test_has_lowercase(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.islower() for char in password))

    def test_has_digit(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.isdigit() for char in password))

    def test_no_spaces(self):
        self.assertFalse(" " in generate_wifi_password())

class FormatReceiptTests(unittest.TestCase):
    def test_receipt_format(self):
        expected =(
            "Чек CampusCoffee\n"
            "Напиток: espresso\n"
            "Количество: 3\n"
            "Итого: 450 руб."
        )
        self.assertEqual(format_receipt("espresso",3),expected)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)


if __name__ == "__main__":
    unittest.main()