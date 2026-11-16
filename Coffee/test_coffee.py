import math
import string
import unittest
from unittest.mock import patch
import coffee

class PriceTests(unittest.TestCase):
    def test_menu_prices(self):
        for name, price in {'espresso':150, 'capuccino':250, 'latte':280,
                            'americano':200, 'tea':120, 'hot_chocolate':220}.items():
            with self.subTest(name=name):
                self.assertEqual(coffee.get_price(name), price)

    def test_unknown_and_empty(self):
        for name in ['', 'unknown', 'Latte', ' latte ']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                coffee.get_price(name)

    def test_invalid_name_types(self):
        for name in [None, 5, True, [], {}]:
            with self.subTest(name=name), self.assertRaises(TypeError):
                coffee.get_price(name)


class TotalTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(coffee.calculate_order_total(3, 150), 450)

    def test_fractional_price(self):
        self.assertAlmostEqual(coffee.calculate_order_total(3, 12.35), 37.05)

    def test_zero(self):
        for q, p in [(0, 150), (2, 0), (0, 0)]:
            with self.subTest(q=q, p=p):
                self.assertEqual(coffee.calculate_order_total(q, p), 0)

    def test_negative(self):
        for q, p in [(-1, 150), (1, -2), (-1, -2)]:
            with self.subTest(q=q, p=p), self.assertRaises(ValueError):
                coffee.calculate_order_total(q, p)

    def test_invalid_types(self):
        for q, p in [(1.5, 150), ('2', 150), (None, 150), (2, '150'), (2, None)]:
            with self.subTest(q=q, p=p), self.assertRaises(TypeError):
                coffee.calculate_order_total(q, p)

    def test_boolean_quantity(self):
        with self.assertRaises(TypeError):
            coffee.calculate_order_total(True, 150)

    def test_boolean_price(self):
        with self.assertRaises(TypeError):
            coffee.calculate_order_total(2, True)

    def test_nonfinite_price(self):
        for p in [math.nan, math.inf, -math.inf]:
            with self.subTest(price=p), self.assertRaises(ValueError):
                coffee.calculate_order_total(2, p)


class MostExpensiveTests(unittest.TestCase):
    def test_regular_menu(self):
        self.assertEqual(coffee.get_most_expensive_drink(), ('latte', 280))

    def test_single_item(self):
        with patch.dict(coffee.MENU, {'tea':120}, clear=True):
            self.assertEqual(coffee.get_most_expensive_drink(), ('tea',120))

    def test_empty_menu(self):
        with patch.dict(coffee.MENU, {}, clear=True), self.assertRaises(ValueError):
            coffee.get_most_expensive_drink()

    def test_empty_menu_message(self):
        with patch.dict(coffee.MENU, {}, clear=True), self.assertRaisesRegex(ValueError, 'Меню пусто'):
            coffee.get_most_expensive_drink()

    def test_tied_prices(self):
        with patch.dict(coffee.MENU, {'first':200, 'second':200}, clear=True):
            self.assertEqual(coffee.get_most_expensive_drink(), ('first',200))


class PasswordTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(coffee.generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(coffee.generate_wifi_password(20)), 20)

    def test_character_contract(self):
        allowed = set(string.ascii_letters + string.digits)
        for _ in range(50):
            password = coffee.generate_wifi_password()
            self.assertTrue(set(password) <= allowed)
            self.assertTrue(any(c in string.ascii_lowercase for c in password))
            self.assertTrue(any(c in string.ascii_uppercase for c in password))
            self.assertTrue(any(c in string.digits for c in password))
            self.assertFalse(any(c.isspace() for c in password))

    def test_short_length(self):
        for n in [-1, 0, 7]:
            with self.subTest(length=n), self.assertRaises(ValueError):
                coffee.generate_wifi_password(n)

    def test_invalid_length_types(self):
        for n in [8.0, '8', None]:
            with self.subTest(length=n), self.assertRaises(TypeError):
                coffee.generate_wifi_password(n)

    def test_boolean_length(self):
        with self.assertRaises(TypeError):
            coffee.generate_wifi_password(True)


class ReceiptTests(unittest.TestCase):
    def test_exact_format(self):
        self.assertEqual(coffee.format_receipt('latte', 2),
                         'Чек CampusCoffee\nНапиток: latte\nКоличество: 2\nИтого: 560 руб.')

    def test_all_menu_totals(self):
        for name, price in coffee.MENU.items():
            with self.subTest(name=name):
                self.assertIn(f'Итого: {price * 3} руб.', coffee.format_receipt(name, 3))

    def test_empty_or_unknown(self):
        for name in ['', 'unknown']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                coffee.format_receipt(name, 1)

    def test_invalid_name_types(self):
        for name in [None, 5, [], {}]:
            with self.subTest(name=name), self.assertRaises(TypeError):
                coffee.format_receipt(name, 1)

    def test_nonpositive_quantity(self):
        for q in [0, -1]:
            with self.subTest(q=q), self.assertRaises(ValueError):
                coffee.format_receipt('tea', q)

    def test_invalid_quantity_types(self):
        for q in [1.5, '2', None]:
            with self.subTest(q=q), self.assertRaises(TypeError):
                coffee.format_receipt('tea', q)

    def test_boolean_quantity(self):
        with self.assertRaises(TypeError):
            coffee.format_receipt('tea', True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
