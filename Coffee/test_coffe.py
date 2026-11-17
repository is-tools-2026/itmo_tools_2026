<<<<<<< HEAD
=======
"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""
>>>>>>> 3bcf942d47ba8d29494a77c899dfc8b711129530

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
<<<<<<< HEAD
)


class GetPriceTestCase(unittest.TestCase):

=======
)   

# Пример
class GetPriceTestCase(unittest.TestCase):
>>>>>>> 3bcf942d47ba8d29494a77c899dfc8b711129530
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

<<<<<<< HEAD
    def test_wrong_type(self):
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

    def test_fractional_price(self):
        self.assertAlmostEqual(
            calculate_order_total(2, 150.25), 300.5
        )


class GetMostExpensiveDrinkTestCase(unittest.TestCase):

    def test_most_expensive_drink(self):
        self.assertEqual(
            get_most_expensive_drink(), ("latte", 280)
        )


class GenerateWifiPasswordTestCase(unittest.TestCase):

    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
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

    def test_allowed_characters(self):
        password = generate_wifi_password()
        self.assertFalse(
            any(not c.isalnum() or not c.isascii() for c in password)
        )

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)


class FormatReceiptTestCase(unittest.TestCase):

    def test_normal_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertEqual(
            receipt,
            "\n---Чек Coffee---\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб.\n"
        )

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 2)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown", 2)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_zero_quantity(self):
        receipt = format_receipt("latte", 0)
        self.assertIn("Итого: 0 руб.", receipt)


if __name__ == "__main__":
    unittest.main()
=======
    def test_empty_name(self):
       with self.assertRaises(ValueError):
           get_price(5)

if __name__ == "__main__":
    unittest.main()
>>>>>>> 3bcf942d47ba8d29494a77c899dfc8b711129530
