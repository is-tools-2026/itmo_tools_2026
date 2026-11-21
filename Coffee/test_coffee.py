import re
import unittest

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

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_all_menu_items(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertEqual(get_price(name), price)

    def test_price_is_positive_int(self):
        self.assertIsInstance(get_price("latte"), int)
        self.assertTrue(get_price("latte") > 0)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_number_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_unhashable_name(self):
        with self.assertRaises(ValueError):
            get_price([])

    def test_case_sensitive(self):
        with self.assertRaises(ValueError):
            get_price("ESPRESSO")

    def test_name_with_spaces(self):
        with self.assertRaises(ValueError):
            get_price(" espresso ")


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_one_item(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_zero_price(self):
        self.assertEqual(calculate_order_total(5, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(calculate_order_total(10**6, 280), 280_000_000)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 99.99), 299.97, places=2)

    def test_result_not_negative(self):
        self.assertFalse(calculate_order_total(2, 100) < 0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(1, -280)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total("3", 280)

    def test_string_drink_instead_of_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total("latte", 5)

    def test_string_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2, "280")

    def test_none_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(None, 280)

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2.5, 280)


class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_returns_latte(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_returns_tuple_of_two(self):
        result = get_most_expensive_drink()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_name_in_menu(self):
        name, _ = get_most_expensive_drink()
        self.assertIn(name, MENU)

    def test_price_is_max(self):
        _, price = get_most_expensive_drink()
        self.assertEqual(price, max(MENU.values()))

    def test_no_drink_is_more_expensive(self):
        _, price = get_most_expensive_drink()
        self.assertTrue(all(price >= p for p in MENU.values()))


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(20)), 20)

    def test_returns_string(self):
        self.assertIsInstance(generate_wifi_password(), str)

    def test_only_latin_letters_and_digits(self):
        for _ in range(200):
            pwd = generate_wifi_password()
            self.assertRegex(pwd, r"^[A-Za-z0-9]+$")

    def test_has_upper_lower_digit(self):
        for _ in range(200):
            pwd = generate_wifi_password()
            self.assertTrue(any(c.isupper() for c in pwd), pwd)
            self.assertTrue(any(c.islower() for c in pwd), pwd)
            self.assertTrue(any(c.isdigit() for c in pwd), pwd)

    def test_passwords_are_random(self):
        passwords = {generate_wifi_password(16) for _ in range(20)}
        self.assertGreater(len(passwords), 1)

    def test_length_too_short(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_length_zero(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_length_negative(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-5)

    def test_length_string(self):
        with self.assertRaises(TypeError):
            generate_wifi_password("8")

    def test_length_none(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(None)

    def test_length_float(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(8.5)


class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_format_regex(self):
        receipt = format_receipt("latte", 2)
        pattern = (r"Чек CampusCoffee\n"
                   r"Напиток: latte\n"
                   r"Количество: 2\n"
                   r"Итого: 560 руб\.")
        self.assertRegex(receipt, pattern)

    def test_receipt_contains_fields(self):
        receipt = format_receipt("espresso", 3)
        self.assertIn("Напиток: espresso", receipt)
        self.assertIn("Количество: 3", receipt)
        self.assertIn("Итого: 450 руб.", receipt)

    def test_receipt_header(self):
        self.assertIn("Чек CampusCoffee", format_receipt("tea", 1))

    def test_receipt_is_string(self):
        self.assertIsInstance(format_receipt("tea", 1), str)

    def test_zero_quantity(self):
        self.assertIn("Итого: 0 руб.", format_receipt("tea", 0))

    def test_total_is_correct_for_every_drink(self):
        for name, price in MENU.items():
            with self.subTest(drink=name):
                self.assertIn(f"Итого: {price * 4} руб.", format_receipt(name, 4))

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("pizza", 1)

    def test_unhashable_name(self):
        with self.assertRaises(ValueError):
            format_receipt(["latte"], 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", "2")

    def test_none_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", None)

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", 2.5)


if __name__ == "__main__":
    unittest.main()
