import unittest
import string

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
)


class GetPriceTestCase(unittest.TestCase):

    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_latte_price(self):
        self.assertEqual(get_price("latte"), 280)

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
        self.assertEqual(calculate_order_total(2, 150), 300)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(2, 150.5), 301.0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_fractional_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(1.5, 150)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("2", 150)


class MostExpensiveDrinkTestCase(unittest.TestCase):

    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))


class GenerateWifiPasswordTestCase(unittest.TestCase):

    def test_default_password_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_custom_password_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)

    def test_password_has_uppercase(self):
        password = generate_wifi_password()
        self.assertTrue(
            any(c in string.ascii_uppercase for c in password)
        )

    def test_password_has_lowercase(self):
        password = generate_wifi_password()
        self.assertTrue(
            any(c in string.ascii_lowercase for c in password)
        )

    def test_password_has_digit(self):
        password = generate_wifi_password()
        self.assertTrue(
            any(c in string.digits for c in password)
        )

    def test_password_has_only_allowed_characters(self):
        password = generate_wifi_password()
        self.assertFalse(
            any(c not in string.ascii_letters + string.digits for c in password)
        )

    def test_password_too_short(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-5)

    def test_invalid_length_type(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("eight")

    def test_fractional_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)


class FormatReceiptTestCase(unittest.TestCase):

    def test_normal_receipt(self):
        receipt = format_receipt("latte", 2)

        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("water", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_zero_quantity(self):
        receipt = format_receipt("latte", 0)
        self.assertIn("Итого: 0 руб.", receipt)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "two")

    def test_fractional_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)


if __name__ == "__main__":
    unittest.main()