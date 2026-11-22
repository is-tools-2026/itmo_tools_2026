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

    def test_empty_name_num(self):
       with self.assertRaises(ValueError):
           get_price(5)


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_two_capuccino(self):
        self.assertEqual(calculate_order_total(2, 250), 500)
    
    def test_two_espresso(self):
        self.assertEqual(calculate_order_total(2, 150), 300)
    
    def test_fractional_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2.5, 150)
    
    def test_fractional_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2, 150.75)
    
    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            calculate_order_total()
    
    def test_zero_quantity(self):      
        self.assertEqual(calculate_order_total(0, 150), 0)
    
    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(2, 0), 0)




class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))




class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_length_below_minimum(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_has_uppercase_letter(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.isupper() for char in password))
    
    def test_has_lowercase_letter(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.islower() for char in password))
    
    def test_has_digit(self):
        password = generate_wifi_password()
        self.assertTrue(any(char.isdigit() for char in password))
    
    def test_only_allowed_characters(self):
        password = generate_wifi_password()
        self.assertTrue(password.isascii() and password.isalnum())
    
    def test_requested_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)



class FormatReceiptTestCase(unittest.TestCase):
    def test_latte_receipt(self):
        receipt = format_receipt("latte", 2)

        expected = (
            "Чек CampusCoffee\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб."
        )
        self.assertEqual(receipt.strip("\n"), expected)

    def test_zero_quantity(self):
        receipt = format_receipt("espresso", 0)
        self.assertIn("Количество: 0", receipt.splitlines())
        self.assertIn("Итого: 0 руб.", receipt.splitlines())

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_fractional_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", 1.5)

    def test_text_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", "два")




if __name__ == "__main__":
    unittest.main()