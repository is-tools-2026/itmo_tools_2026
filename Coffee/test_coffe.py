import string
import unittest
from unittest.mock import patch

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)

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

    def test_number_instead_of_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_list_instead_of_name(self):
        with self.assertRaises(ValueError):
            get_price(["latte"])


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_total(self):
        self.assertAlmostEqual(calculate_order_total(3, 150), 450)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(3, 0), 0)

    def test_negative_quantity(self):
        with self.assertRaisesRegex(ValueError, "Количество"):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaisesRegex(ValueError, "Цена"):
            calculate_order_total(3, -150)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("3", 150)

    def test_fractional_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(3, 150.5)


class MostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_in_menu(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_one_drink(self):
        with patch("coffee.MENU", {"tea": 120}):
            self.assertEqual(get_most_expensive_drink(), ("tea", 120))

    def test_uses_price(self):
        with patch("coffee.MENU", {"z": 100, "a": 200}):
            self.assertEqual(get_most_expensive_drink(), ("a", 200))


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_password_characters(self):
        password = generate_wifi_password()
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertFalse(any(c not in string.ascii_letters + string.digits for c in password))

    def test_short_password(self):
        with self.assertRaisesRegex(ValueError, "не меньше 8"):
            generate_wifi_password(7)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")


class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_contents(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек", receipt)
        self.assertRegex(receipt, r"Напиток: latte\nКоличество: 2\nИтого: 560 руб\.\n$")

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", format_receipt("tea", 0))

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_fractional_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)


if __name__ == "__main__":
    unittest.main()
