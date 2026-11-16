"""Проверки модуля кофейни для лабораторной №4, ИСУ 414791."""

import math
from pathlib import Path
import string
import subprocess
import sys
import unittest
from unittest.mock import patch

if __package__:
    from . import coffee
else:
    import coffee


class GetPriceTests(unittest.TestCase):
    def test_prices_from_menu(self):
        expected = {"espresso": 150, "capuccino": 250, "latte": 280,
                    "americano": 200, "tea": 120, "hot_chocolate": 220}
        for name, price in expected.items():
            self.assertEqual(coffee.get_price(name), price)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            coffee.get_price("water")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            coffee.get_price("")

    def test_number_instead_of_name(self):
        with self.assertRaises(ValueError):
            coffee.get_price(5)

    def test_list_instead_of_name(self):
        with self.assertRaises(ValueError):
            coffee.get_price(["latte"])

    def test_dictionary_instead_of_name(self):
        with self.assertRaises(ValueError):
            coffee.get_price({"name": "latte"})

    def test_none_instead_of_name(self):
        with self.assertRaises(ValueError):
            coffee.get_price(None)

    def test_name_must_match_menu(self):
        with self.assertRaises(ValueError):
            coffee.get_price("LATTE")


class OrderTotalTests(unittest.TestCase):
    def test_regular_order(self):
        self.assertEqual(coffee.calculate_order_total(3, 280), 840)

    def test_zero_quantity(self):
        self.assertEqual(coffee.calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(coffee.calculate_order_total(3, 0), 0)

    def test_fractional_price(self):
        self.assertAlmostEqual(coffee.calculate_order_total(3, 10.1), 30.3)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(-1, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(1, -280)

    def test_fractional_quantity(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(1.5, 280)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total("latte", 5)

    def test_string_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(2, "280")

    def test_boolean_quantity(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(True, 280)

    def test_boolean_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(2, False)

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(None, 280)

    def test_none_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(2, None)

    def test_nan_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(2, math.nan)

    def test_infinite_price(self):
        with self.assertRaises(ValueError):
            coffee.calculate_order_total(2, math.inf)


class MostExpensiveDrinkTests(unittest.TestCase):
    def test_regular_menu(self):
        self.assertEqual(coffee.get_most_expensive_drink(), ("latte", 280))

    def test_single_drink(self):
        with patch.dict(coffee.MENU, {"tea": 120}, clear=True):
            self.assertEqual(coffee.get_most_expensive_drink(), ("tea", 120))

    def test_other_menu(self):
        with patch.dict(coffee.MENU, {"a": 500, "b": 10, "c": 200}, clear=True):
            self.assertEqual(coffee.get_most_expensive_drink(), ("a", 500))

    def test_equal_prices(self):
        with patch.dict(coffee.MENU, {"a": 100, "b": 100}, clear=True):
            name, price = coffee.get_most_expensive_drink()
            self.assertIn(name, ("a", "b"))
            self.assertEqual(price, 100)

    def test_empty_menu(self):
        with patch.dict(coffee.MENU, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "Меню пусто"):
                coffee.get_most_expensive_drink()

    def test_menu_is_not_changed(self):
        original = coffee.MENU.copy()
        coffee.get_most_expensive_drink()
        self.assertEqual(coffee.MENU, original)


class WifiPasswordTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(coffee.generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(coffee.generate_wifi_password(20)), 20)

    def test_only_latin_letters_and_digits(self):
        allowed = set(string.ascii_letters + string.digits)
        password = coffee.generate_wifi_password(32)
        self.assertTrue(set(password) <= allowed)
        self.assertFalse(any(char.isspace() for char in password))

    def test_required_character_groups(self):
        for _ in range(20):
            password = coffee.generate_wifi_password()
            self.assertTrue(any(char in string.ascii_lowercase for char in password))
            self.assertTrue(any(char in string.ascii_uppercase for char in password))
            self.assertTrue(any(char in string.digits for char in password))

    def test_seven_characters(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(-8)

    def test_fractional_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(8.5)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password("8")

    def test_none_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(None)

    def test_boolean_length(self):
        with self.assertRaises(ValueError):
            coffee.generate_wifi_password(True)


class ReceiptTests(unittest.TestCase):
    def test_receipt_matches_documented_format(self):
        self.assertEqual(
            coffee.format_receipt("latte", 2),
            "Чек CampusCoffee\nНапиток: latte\nКоличество: 2\nИтого: 560 руб.",
        )

    def test_other_drink_total(self):
        self.assertIn("Итого: 360 руб.", coffee.format_receipt("tea", 3))

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", coffee.format_receipt("latte", 0))

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("water", 1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("latte", -1)

    def test_fractional_quantity(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("latte", 1.5)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("latte", "2")

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("latte", None)

    def test_boolean_quantity(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt("latte", True)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt(["latte"], 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            coffee.format_receipt(None, 1)


class ModuleImportTests(unittest.TestCase):
    def test_import_has_no_output(self):
        result = subprocess.run(
            [sys.executable, "-c", "import coffee"],
            cwd=Path(coffee.__file__).parent,
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
