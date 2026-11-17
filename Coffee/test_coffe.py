import string
import unittest

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
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
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


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        password = generate_wifi_password()
        self.assertIsInstance(password, str)
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_password_characters(self):
        password = generate_wifi_password()
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_other_character = False

        for character in password:
            if character in string.ascii_lowercase:
                has_lowercase = True
            elif character in string.ascii_uppercase:
                has_uppercase = True
            elif character in string.digits:
                has_digit = True
            else:
                has_other_character = True

        self.assertTrue(has_lowercase)
        self.assertTrue(has_uppercase)
        self.assertTrue(has_digit)
        self.assertFalse(has_other_character)

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")


class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_contents(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек", receipt)
        expected_lines = ["Напиток: latte", "Количество: 2", "Итого: 560 руб."]
        self.assertEqual(receipt.splitlines()[-3:], expected_lines)

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
