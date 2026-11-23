"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    apply_discount,
    calculate_bonus,
    use_bonus,
    is_menu_item_available,
    get_most_expensive_drink,
    get_cheapest_drink,
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

    def test_empty_name(self):
       with self.assertRaises(ValueError):
           get_price(5)



