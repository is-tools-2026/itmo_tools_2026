
"""Unit-тесты для модуля вузовской кофейни CampusCoffee."""

import string
import unittest

from coffee import (
    MENU,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


class GetPriceTest(unittest.TestCase):

    def test_all_menu_items(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertEqual(get_price(name), price)

    def test_price_positive(self):
        self.assertTrue(get_price("latte") > 0)

    def test_invalid_names(self):
        bad_names = [
            "unknown", "", "ESPRESSO",
            " latte ", 5, None, ["latte"]
        ]

        for name in bad_names:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    get_price(name)


class CalculateOrderTotalTest(unittest.TestCase):

    def test_normal_calculation(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(5, 0), 0)

    def test_average_price(self):
        total = calculate_order_total(3, 280)
        self.assertAlmostEqual(total / 3, 280)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

        with self.assertRaises(ValueError):
            calculate_order_total(2, -280)

    def test_invalid_types(self):
        cases = [
            ("latte", 5),
            (5, "280"),
            (None, 280),
            (2, None),
            (1.5, 280),
            (True, 280),
        ]

        for quantity, price in cases:
            with self.subTest(quantity=quantity, price=price):
                with self.assertRaises(ValueError):
                    calculate_order_total(quantity, price)


class GetMostExpensiveDrinkTest(unittest.TestCase):

    def test_returns_latte(self):
        self.assertEqual(
            get_most_expensive_drink(),
            ("latte", 280)
        )

    def test_price_is_maximum(self):
        name, price = get_most_expensive_drink()

        self.assertEqual(price, max(MENU.values()))
        self.assertEqual(price, MENU[name])


class GenerateWifiPasswordTest(unittest.TestCase):

    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(20)), 20)

    def test_only_latin_letters_and_digits(self):
        allowed = set(string.ascii_letters + string.digits)

        for _ in range(30):
            password = generate_wifi_password(12)
            self.assertFalse(set(password) - allowed)

    def test_required_character_classes(self):
        for _ in range(30):
            password = generate_wifi_password(8)

            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))

    def test_invalid_length(self):
        bad_lengths = [7, 0, -5, "8", None, 8.5, True]

        for length in bad_lengths:
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_wifi_password(length)


class FormatReceiptTest(unittest.TestCase):

    def test_exact_receipt(self):
        expected = (
            "Чек CampusCoffee\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб."
        )

        self.assertEqual(
            format_receipt("latte", 2).strip(),
            expected
        )

    def test_receipt_for_espresso(self):
        receipt = format_receipt("espresso", 3)

        self.assertIn("Напиток: espresso", receipt)
        self.assertIn("Количество: 3", receipt)
        self.assertIn("Итого: 450 руб.", receipt)

    def test_zero_quantity(self):
        self.assertIn(
            "Итого: 0 руб.",
            format_receipt("tea", 0)
        )

    def test_invalid_drink(self):
        bad_names = ["", "pizza", None, ["latte"], " latte "]

        for name in bad_names:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    format_receipt(name, 1)

    def test_invalid_quantity(self):
        bad_quantities = [-1, "2", None, 1.5, True]

        for quantity in bad_quantities:
            with self.subTest(quantity=quantity):
                with self.assertRaises(ValueError):
                    format_receipt("latte", quantity)


if __name__ == "__main__":
    unittest.main()
