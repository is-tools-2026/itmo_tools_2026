"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    format_receipt,
    generate_wifi_password
)

# Пример
class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_latte_price(self):
        self.assertEqual(get_price("latte"), 280)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_incorrect_name_type(self):
       with self.assertRaises(ValueError):
           get_price(5)

class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_correct_output(self):
        self.assertEqual(calculate_order_total(2, 280), 560)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 120), 0)
        
    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-5, 120)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(5, -120)

    def test_incorrect_quantity_type(self):
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 120)

    def test_incorrect_price_type(self):
        with self.assertRaises(ValueError):
            calculate_order_total(5, "120")

class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_password_characters(self):
        password = generate_wifi_password()
        self.assertTrue(all(
            char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            for char in password
        ))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(any(char.isspace() for char in password))

    def test_short_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-1)