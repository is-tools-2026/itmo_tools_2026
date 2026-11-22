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

#Тесты для функции get_price
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

    def  test_invalid_type(self):
       with self.assertRaises(ValueError):
           get_price(5)


# Тесты для функции calculate_order_total
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_valid_total(self):
        self.assertEqual(calculate_order_total(3, 150), 450)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("3", 150)



# Тесты для функции get_most_expensive_drink
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_result_is_tuple(self):
        result = get_most_expensive_drink()
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 2)


# Тесты для функции generate_wifi_password
class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_password_length(self):
        pwd = generate_wifi_password(8)
        self.assertEqual(len(pwd), 8)

    def test_password_contains_digit(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(any(char.isdigit() for char in pwd))

    def test_password_contains_upper_and_lower(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(any(char.isupper() for char in pwd))
        self.assertTrue(any(char.islower() for char in pwd))

    def test_short_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(5)

    def test_invalid_length_type(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")


# Тесты для функции format_receipt
class FormatReceiptTestCase(unittest.TestCase):
    def test_valid_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек", receipt)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560", receipt)

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 2)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("water", 2)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_invalid_quantity_type(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")


if __name__ == "__main__":
    unittest.main()