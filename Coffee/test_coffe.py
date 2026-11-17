"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest
import re

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
)


# Пример (исправлено дублирование имени метода test_empty_name)
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

    def test_invalid_type_name(self):
        with self.assertRaises(ValueError):
            get_price(5)


# ============================================================
# ТЕСТЫ ФУНКЦИИ 1. calculate_order_total
# ============================================================
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_valid_total(self):
        self.assertEqual(calculate_order_total(3, 200), 600)
        self.assertAlmostEqual(calculate_order_total(2, 150.0), 300.0)

    def test_zero_quantity_or_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(0, 200)
        with self.assertRaises(ValueError):
            calculate_order_total(2, 0)

    def test_negative_quantity_or_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-3, 200)
        with self.assertRaises(ValueError):
            calculate_order_total(3, -200)

    def test_invalid_types(self):
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 5)
        with self.assertRaises(ValueError):
            calculate_order_total(2, "200")
        with self.assertRaises(ValueError):
            calculate_order_total(True, 200)


# ============================================================
# ТЕСТЫ ФУНКЦИИ 2. get_most_expensive_drink
# ============================================================
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)
        self.assertTrue(price == 280)
        self.assertFalse(name == "tea")


# ============================================================
# ТЕСТЫ ФУНКЦИИ 3. generate_wifi_password
# ============================================================
class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        pwd = generate_wifi_password()
        self.assertEqual(len(pwd), 8)

    def test_custom_length(self):
        pwd = generate_wifi_password(12)
        self.assertEqual(len(pwd), 12)

    def test_password_characters(self):
        pwd = generate_wifi_password(10)
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(pwd.isalnum())

    def test_short_length_raises(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)
        with self.assertRaises(ValueError):
            generate_wifi_password(0)
        with self.assertRaises(ValueError):
            generate_wifi_password(-5)

    def test_invalid_type_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)
        with self.assertRaises(ValueError):
            generate_wifi_password(True)


# ============================================================
# ТЕСТЫ ФУНКЦИИ 4. format_receipt
# ============================================================
class FormatReceiptTestCase(unittest.TestCase):
    def test_valid_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек CampusCoffee", receipt)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)
        pattern = r"Чек CampusCoffee.*Напиток: latte\s+Количество: 2\s+Итого: 560 руб\."
        self.assertRegex(receipt, re.compile(pattern, re.DOTALL))

    def test_empty_or_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_zero_or_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)
        with self.assertRaises(ValueError):
            format_receipt("latte", -2)

    def test_invalid_types(self):
        with self.assertRaises(ValueError):
            format_receipt(123, 1)
        with self.assertRaises(ValueError):
            format_receipt("latte", "один")
        with self.assertRaises(ValueError):
            format_receipt("latte", True)


if __name__ == "__main__":
    unittest.main()