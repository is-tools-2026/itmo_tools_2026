"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».
"""

import unittest

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


# Пример
class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_latte_price(self):
        self.assertEqual(get_price("latte"), 280)

    def test_americano_price(self):
        self.assertEqual(get_price("americano"), 200)

    def test_tea_price(self):
        self.assertEqual(get_price("tea"), 120)

    def test_hot_chocolate_price(self):
        self.assertEqual(get_price("hot_chocolate"), 220)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_number_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            get_price(["latte"])

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)


# №1 Расчёт стоимости заказа
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_calculate_order_total(self):
        result = calculate_order_total(2, 250)
        self.assertEqual(result, 500)

    def test_one_drink(self):
        self.assertEqual(calculate_order_total(1, 280), 280)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 250), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(2, 0), 0)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 150.1), 450.3)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 250)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -250)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("2", 250)

    def test_empty_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("", 250)

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(1.5, 250)

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(None, 250)

    def test_string_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, "250")

    def test_empty_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, "")

    def test_none_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, None)


# №2 Самый дорогой напиток
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_most_expensive_drink(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))


# №3 Пароль от Wi-Fi
class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        password = generate_wifi_password()
        self.assertEqual(len(password), 8)

    def test_custom_length(self):
        password = generate_wifi_password(12)
        self.assertEqual(len(password), 12)

    def test_only_latin_letters_and_digits(self):
        password = generate_wifi_password()
        self.assertTrue(password.isascii())
        self.assertTrue(password.isalnum())

    def test_uppercase_letter(self):
        self.assertRegex(generate_wifi_password(), r"[A-Z]")

    def test_lowercase_letter(self):
        self.assertRegex(generate_wifi_password(), r"[a-z]")

    def test_digit(self):
        self.assertRegex(generate_wifi_password(), r"[0-9]")

    def test_no_spaces(self):
        self.assertFalse(" " in generate_wifi_password())

    def test_short_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-8)

    def test_string_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("8")

    def test_empty_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password("")

    def test_float_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)

    def test_none_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(None)


# №4 Чек
class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt(self):
        expected = (
            "Чек CampusCoffee\n"
            "Напиток: latte\n"
            "Количество: 2\n"
            "Итого: 560 руб.\n"
        )
        self.assertEqual(format_receipt("latte", 2), expected)

    def test_zero_quantity(self):
        expected = (
            "Чек CampusCoffee\n"
            "Напиток: tea\n"
            "Количество: 0\n"
            "Итого: 0 руб.\n"
        )
        self.assertEqual(format_receipt("tea", 0), expected)

    def test_receipt_format(self):
        receipt = format_receipt("espresso", 3)
        self.assertRegex(receipt, r"Итого: 450 руб\.")

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown_drink", 1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_number_name(self):
        with self.assertRaises(ValueError):
            format_receipt(5, 1)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            format_receipt(["latte"], 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_string_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "2")

    def test_empty_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", "")

    def test_float_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_none_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", None)


if __name__ == "__main__":
    unittest.main()
