
import unittest
import re

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
        self.assertEqual(calculate_order_total(3, 150), 450)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(3, 0), 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -100)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            calculate_order_total("5", 100)


class MostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_result_format(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_password_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_password_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_password_has_uppercase(self):
        self.assertTrue(any(c.isupper() for c in generate_wifi_password()))

    def test_password_has_lowercase(self):
        self.assertTrue(any(c.islower() for c in generate_wifi_password()))

    def test_password_has_digit(self):
        self.assertTrue(any(c.isdigit() for c in generate_wifi_password()))

    def test_password_characters(self):
        password = generate_wifi_password(10)
        self.assertTrue(re.fullmatch(r"[A-Za-z0-9]+", password))

    def test_short_password(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)


class FormatReceiptTestCase(unittest.TestCase):
    def test_normal_receipt(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", format_receipt("latte", 0))

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("water", 1)


if __name__ == "__main__":
    unittest.main()
