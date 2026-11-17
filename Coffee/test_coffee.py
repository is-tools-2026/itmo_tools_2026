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
        for bad in ["unknown", "", "ESPRESSO", " latte ", 5, None, ["latte"]]:
            with self.subTest(name=bad):
                with self.assertRaises(ValueError):
                    get_price(bad)


class CalculateOrderTotalTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_zeros(self):
        self.assertEqual(calculate_order_total(0, 280), 0)
        self.assertEqual(calculate_order_total(5, 0), 0)

    def test_average_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 280) / 3, 280)

    def test_invalid_args(self):
        cases = [(-1, 280), (2, -280), ("latte", 5), (5, "280"),
                 (None, 280), (2, None), (1.5, 280), (True, 280)]
        for quantity, price in cases:
            with self.subTest(quantity=quantity, price=price):
                with self.assertRaises(ValueError):
                    calculate_order_total(quantity, price)


class GetMostExpensiveDrinkTest(unittest.TestCase):
    def test_returns_latte(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_price_is_max(self):
        self.assertTrue(get_most_expensive_drink()[1] == max(MENU.values()))


class GenerateWifiPasswordTest(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)
        self.assertEqual(len(generate_wifi_password(20)), 20)

    def test_only_latin_and_digits(self):
        allowed = set(string.ascii_letters + string.digits)
        for _ in range(50):
            self.assertFalse(set(generate_wifi_password(12)) - allowed)

    def test_has_required_classes(self):
        for _ in range(50):
            pwd = generate_wifi_password(8)
            with self.subTest(pwd=pwd):
                self.assertTrue(any(c.islower() for c in pwd))
                self.assertTrue(any(c.isupper() for c in pwd))
                self.assertTrue(any(c.isdigit() for c in pwd))

    def test_passwords_differ(self):
        self.assertGreater(len({generate_wifi_password(16) for _ in range(20)}), 1)

    def test_invalid_length(self):
        for bad in [7, 0, -5, "8", None, 8.5]:
            with self.subTest(length=bad):
                with self.assertRaises(ValueError):
                    generate_wifi_password(bad)


class FormatReceiptTest(unittest.TestCase):
    def test_exact_text(self):
        expected = ("Чек CampusCoffee\nНапиток: latte\n"
                    "Количество: 2\nИтого: 560 руб.")
        self.assertEqual(format_receipt("latte", 2).strip(), expected)

    def test_regex_format(self):
        pattern = (r"Чек CampusCoffee\s+Напиток: espresso\s+"
                   r"Количество: 3\s+Итого: 450 руб\.")
        self.assertRegex(format_receipt("espresso", 3), pattern)

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", format_receipt("tea", 0))

    def test_invalid_args(self):
        cases = [("", 1), ("pizza", 1), (None, 1), (["latte"], 1),
                 ("latte", -1), ("latte", "2"), ("latte", None), ("latte", 1.5)]
        for name, quantity in cases:
            with self.subTest(name=name, quantity=quantity):
                with self.assertRaises(ValueError):
                    format_receipt(name, quantity)


if __name__ == "__main__":
    unittest.main()