import re
import string
import unittest
from unittest.mock import patch

from coffee import (
    MENU,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_every_menu_item(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertEqual(get_price(name), price)

    def test_price_is_positive_int(self):
        for name in MENU:
            with self.subTest(drink=name):
                price = get_price(name)
                self.assertIsInstance(price, int)
                self.assertGreater(price, 0)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_wrong_case(self):
        with self.assertRaises(ValueError):
            get_price("Espresso")

    def test_non_string_name(self):
        with self.assertRaises(ValueError):
            get_price(5)
        with self.assertRaises(ValueError):
            get_price(None)


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_single_drink(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(3, 0), 0)

    def test_average_price(self):
        total = calculate_order_total(3, 280)
        self.assertAlmostEqual(total / 3, 280)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-3, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(3, -280)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total("latte", 5)

    def test_string_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(3, "a")

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(1.5, 100)

    def test_none_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(None, 100)


class MostExpensiveDrinkTestCase(unittest.TestCase):
    def test_returns_tuple_of_two(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_most_expensive_is_latte(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_price_is_maximum(self):
        _, price = get_most_expensive_drink()
        self.assertTrue(all(price >= p for p in MENU.values()))

    def test_name_is_in_menu(self):
        name, _ = get_most_expensive_drink()
        self.assertIn(name, MENU)

    def test_with_new_expensive_drink(self):
        with patch.dict(MENU, {"gold_coffee": 999}):
            self.assertEqual(get_most_expensive_drink(), ("gold_coffee", 999))


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        for length in (8, 12, 30):
            with self.subTest(length=length):
                self.assertEqual(len(generate_wifi_password(length)), length)

    def test_only_latin_letters_and_digits(self):
        allowed = set(string.ascii_letters + string.digits)
        for _ in range(200):
            password = generate_wifi_password()
            self.assertTrue(set(password) <= allowed)
            self.assertFalse(any(c in string.punctuation for c in password))
            self.assertNotIn(" ", password)

    def test_has_upper_lower_digit(self):
        for _ in range(200):
            password = generate_wifi_password(8)
            self.assertTrue(any(c.islower() for c in password))
            self.assertTrue(any(c.isupper() for c in password))
            self.assertTrue(any(c.isdigit() for c in password))

    def test_matches_regex(self):
        pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{8}"
        for _ in range(100):
            self.assertRegex(generate_wifi_password(8), pattern)

    def test_passwords_are_random(self):
        passwords = {generate_wifi_password() for _ in range(20)}
        self.assertGreater(len(passwords), 1)

    def test_too_short(self):
        for length in (7, 3, 0, -1):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_wifi_password(length)

    def test_wrong_type(self):
        for bad in ("8", None, 8.5):
            with self.subTest(value=bad):
                with self.assertRaises(TypeError):
                    generate_wifi_password(bad)


class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_contains_data(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_receipt_format_regex(self):
        receipt = format_receipt("latte", 2)
        self.assertRegex(
            receipt, r"Напиток: latte\nКоличество: 2\nИтого: 560 руб\.\n"
        )

    def test_total_for_each_drink(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertIn(f"Итого: {price * 3} руб.", format_receipt(name, 3))

    def test_header_matches_docstring(self):
        self.assertIn("Чек CampusCoffee", format_receipt("tea", 1))

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("pizza", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("tea", -1)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("tea", 0)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("tea", "2")

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("tea", 1.5)


if __name__ == "__main__":
    unittest.main()