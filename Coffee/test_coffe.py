"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    format_receipt,
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
