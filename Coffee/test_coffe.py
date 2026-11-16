import unittest
from unittest.mock import patch

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
    MENU,
)


class TestCoffee(unittest.TestCase):

    def test_get_price_valid(self):
        self.assertEqual(get_price("espresso"), 150)
        self.assertEqual(get_price("latte"), 280)

    def test_get_price_unknown(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")
        with self.assertRaises(ValueError):
            get_price("")

    def test_get_price_invalid_type(self):
        for value in (123, None, True, [], {}):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    get_price(value)

    def test_calculate_total_valid(self):
        self.assertEqual(calculate_order_total(2, 150), 300)
        self.assertEqual(calculate_order_total(0, 150), 0)

    def test_calculate_total_negative(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 150)
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_calculate_total_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_order_total("2", 150)
        with self.assertRaises(TypeError):
            calculate_order_total(2, "150")

    def test_calculate_total_zero_price(self):
        self.assertEqual(calculate_order_total(3, 0), 0)

    def test_calculate_total_float_price(self):
        self.assertAlmostEqual(
            calculate_order_total(3, 10.1), 30.3, places=2
        )

    def test_calculate_total_bool_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(True, 150)

    def test_calculate_total_bool_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2, True)

    def test_calculate_total_float_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(1.5, 150)

    def test_most_expensive_drink(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)
        self.assertTrue(price >= max(MENU.values()))

    def test_most_expensive_empty_menu(self):
        with patch.dict(MENU, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "Меню пустое"):
                get_most_expensive_drink()

    def test_most_expensive_changed_menu(self):
        with patch.dict(MENU, {"tea": 120, "espresso": 350}, clear=True):
            self.assertEqual(
                get_most_expensive_drink(), ("espresso", 350)
            )

    def test_wifi_password_length(self):
        self.assertEqual(len(generate_wifi_password(8)), 8)
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_wifi_password_complexity(self):
        password = generate_wifi_password(8)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))

    def test_wifi_password_invalid_length(self):
        for length in (-1, 0, 7):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    generate_wifi_password(length)

    def test_wifi_password_invalid_type(self):
        for length in ("8", 8.0, None):
            with self.subTest(length=length):
                with self.assertRaises(TypeError):
                    generate_wifi_password(length)

    def test_wifi_password_bool_length(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(True)

    def test_wifi_password_allowed_characters(self):
        password = generate_wifi_password(100)
        self.assertTrue(password.isascii())
        self.assertTrue(password.isalnum())

    def test_wifi_password_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_format_receipt_valid(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек CampusCoffee", receipt)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_format_receipt_invalid(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)
        with self.assertRaises(ValueError):
            format_receipt("unknown", 1)
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)
        with self.assertRaises(TypeError):
            format_receipt("latte", "2")

    def test_format_receipt_exact_format(self):
        expected = (
            "Чек CampusCoffee\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб."
        )
        self.assertEqual(format_receipt("latte", 2), expected)

    def test_format_receipt_invalid_name_type(self):
        for value in (123, None, True, [], {}):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    format_receipt(value, 1)

    def test_format_receipt_bool_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", True)

    def test_format_receipt_float_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", 1.5)

    def test_assert_false_example(self):
        name, price = get_most_expensive_drink()
        self.assertFalse(name == "tea")
        self.assertFalse(price < 280)

    def test_assert_almost_equal_example(self):
        price = get_price("latte")
        calculated_price = price * 0.9
        self.assertAlmostEqual(calculated_price, 252.0, places=1)


if __name__ == "__main__":
    unittest.main()