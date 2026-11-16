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

    def test_normal_order(self):
        self.assertEqual(calculate_order_total(3, 150), 450)

    def test_one_drink(self):
        self.assertEqual(calculate_order_total(1, 200), 200)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_invalid_quantity(self):
        with self.assertRaises((TypeError, ValueError)):
            calculate_order_total("два", 150)

from unittest.mock import patch


class GetMostExpensiveDrinkTestCase(unittest.TestCase):

    def test_most_expensive_drink(self):
        self.assertEqual(
            get_most_expensive_drink(),
            ("latte", 280)
        )

    def test_custom_menu(self):
        with patch.dict(
            "coffee.MENU",
            {"coffee": 100, "tea": 200},
            clear=True
        ):
            self.assertEqual(
                get_most_expensive_drink(),
                ("tea", 200)
            )

    def test_empty_menu(self):
        with patch.dict("coffee.MENU", {}, clear=True):
            with self.assertRaises(ValueError):
                get_most_expensive_drink()

from unittest.mock import patch


class GetMostExpensiveDrinkTestCase(unittest.TestCase):

    def test_most_expensive_drink(self):
        self.assertEqual(
            get_most_expensive_drink(),
            ("latte", 280)
        )

    def test_custom_menu(self):
        with patch.dict(
            "coffee.MENU",
            {"coffee": 100, "tea": 200},
            clear=True
        ):
            self.assertEqual(
                get_most_expensive_drink(),
                ("tea", 200)
            )

    def test_empty_menu(self):
        with patch.dict("coffee.MENU", {}, clear=True):
            with self.assertRaises(ValueError):
                get_most_expensive_drink()


class GenerateWifiPasswordTestCase(unittest.TestCase):

    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)

    def test_uppercase(self):
        password = generate_wifi_password(12)
        self.assertTrue(any(c.isupper() for c in password))

    def test_lowercase(self):
        password = generate_wifi_password(12)
        self.assertTrue(any(c.islower() for c in password))

    def test_digit(self):
        password = generate_wifi_password(12)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_only_allowed_characters(self):
        password = generate_wifi_password(12)
        self.assertTrue(password.isascii())
        self.assertTrue(password.isalnum())
        self.assertFalse(any(c.isspace() for c in password))

    def test_short_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_invalid_float(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(7.5)

    def test_invalid_bool(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(True)



class FormatReceiptTestCase(unittest.TestCase):

    def test_normal_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertTrue("latte" in receipt)
        self.assertTrue("2" in receipt)
        self.assertTrue("560" in receipt)

    def test_receipt_total(self):
        receipt = format_receipt("espresso", 3)
        self.assertTrue("450" in receipt)

    def test_receipt_is_string(self):
        receipt = format_receipt("tea", 1)
        self.assertTrue(isinstance(receipt, str))

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown", 2)

    def test_empty_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("", 2)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)

    def test_invalid_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", "два")

    def test_boolean_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", True)
