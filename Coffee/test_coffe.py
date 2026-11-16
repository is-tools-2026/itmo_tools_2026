"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    # apply_discount,              # Закомментированные функции не тестируем, так как они не используются в коде
    # calculate_bonus,
    # use_bonus,
    # is_menu_item_available,
    get_most_expensive_drink,
    # get_cheapest_drink,
    format_receipt,
    generate_wifi_password,
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


# ФУНКЦИЯ 1.
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_calculate_order_total(self):
        self.assertEqual(calculate_order_total(2, 150), 300)
        self.assertEqual(calculate_order_total(0, 150), 0)
        with self.assertRaises(ValueError):
            calculate_order_total(-1,150)
        with self.assertRaises(ValueError):
            calculate_order_total(1,-150)
    def test_teacher_discount(self):
        self.assertEqual(calculate_order_total(2, 200, "TEACHER15"), 340)

    def test_happy_hour_discount(self):
        self.assertEqual(calculate_order_total(2, 200, "HAPPY_HOUR"), 320)

    def test_first_order_discount(self):
        self.assertEqual(calculate_order_total(2, 200, "FIRST_ORDER"), 380)

    def test_invalid_promocode(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, 200, "INVALID")

    def test_without_promocode(self):
        self.assertEqual(calculate_order_total(2, 200), 400)

class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_get_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))
    def test_result_is_tuple(self):
        self.assertTrue(isinstance(get_most_expensive_drink(), tuple))
    def test_result_has_two_elements(self):
        self.assertEqual(len(get_most_expensive_drink()), 2)

class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_password_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)
    def test_custom_password_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)
    def test_password_contains_required_characters(self):
        password = generate_wifi_password()

        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(password.islower())
    def test_password_too_short(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)
class FormatReceiptTestCase(unittest.TestCase):
    def test_format_receipt(self):
        receipt = format_receipt("latte", 1)
        self.assertTrue("Напиток: latte" in receipt)
        self.assertTrue("Количество: 1" in receipt)
        self.assertTrue("Итого: 280 руб." in receipt)
    def test_zero_quantity(self):
        receipt = format_receipt("latte", 0)
        self.assertTrue("Итого: 0 руб." in receipt)
    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)
    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_nonexistent_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("juice", 1)
    def test_receipt_with_student_discount(self):
        receipt = format_receipt("latte", 1, "STUDENT10")
        self.assertTrue("Скидка: 28.0 руб." in receipt)
        self.assertTrue("Итого: 252.0 руб." in receipt)

    def test_receipt_with_teacher_discount(self):
        receipt = format_receipt("latte", 1, "TEACHER15")
        self.assertTrue("Скидка: 42.0 руб." in receipt)
        self.assertTrue("Итого: 238.0 руб." in receipt)

    def test_receipt_with_invalid_promocode(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1, "INVALID")

    def test_receipt_without_promocode(self):
        receipt = format_receipt("latte", 1)
        self.assertTrue("Итого: 280 руб." in receipt)