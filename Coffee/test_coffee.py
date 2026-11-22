"""
Unit-тесты для модуля вузовской кофейни «CampusCoffee».

Тесты написаны под ОЖИДАЕМОЕ (корректное) поведение функций.
Падения тестов на текущей версии coffee.py = найденные баги.
"""

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


# ============================================================
# 0. get_price — цена напитка по названию
# ============================================================
class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_latte_price(self):
        self.assertEqual(get_price("latte"), 280)

    def test_tea_price(self):
        self.assertEqual(get_price("tea"), 120)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_non_string_name(self):
        with self.assertRaises(ValueError):
            get_price(5)


# ============================================================
# 1. calculate_order_total — стоимость заказа
# ============================================================
class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_normal_order(self):
        self.assertEqual(calculate_order_total(3, 200), 600)

    def test_single_item(self):
        self.assertEqual(calculate_order_total(1, 150), 150)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 200), 0)

    def test_negative_quantity(self):
        # БАГ: сейчас вернёт -200 вместо ValueError
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 200)

    def test_negative_price(self):
        # БАГ: сейчас вернёт -600 вместо ValueError
        with self.assertRaises(ValueError):
            calculate_order_total(3, -200)

    def test_string_quantity(self):
        # БАГ: сейчас TypeError вместо ValueError
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total("3", 200)

    def test_float_quantity(self):
        # БАГ: сейчас вернёт 700.0 — количество должно быть целым
        with self.assertRaises(ValueError):
            calculate_order_total(3.5, 200)

    def test_none_quantity(self):
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total(None, 200)

    def test_result_is_int(self):
        self.assertTrue(isinstance(calculate_order_total(2, 150), int))


# ============================================================
# 2. get_most_expensive_drink — самый дорогой напиток
# ============================================================
class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_returns_tuple(self):
        result = get_most_expensive_drink()
        self.assertTrue(isinstance(result, tuple))
        self.assertEqual(len(result), 2)

    def test_most_expensive_is_latte(self):
        # БАГ: сейчас min() вернёт ('tea', 120) — самый дешёвый
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")

    def test_price_matches_max(self):
        # БАГ: сейчас вернёт 120 вместо 280
        _, price = get_most_expensive_drink()
        self.assertEqual(price, max(MENU.values()))

    def test_price_is_max_value(self):
        _, price = get_most_expensive_drink()
        self.assertEqual(price, 280)

    def test_name_in_menu(self):
        name, _ = get_most_expensive_drink()
        self.assertIn(name, MENU)


# ============================================================
# 3. generate_wifi_password — пароль от Wi-Fi
# ============================================================
class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_custom_length(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_contains_lowercase(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(any(c.islower() for c in pwd))

    def test_contains_uppercase(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(any(c.isupper() for c in pwd))

    def test_contains_digit(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(any(c.isdigit() for c in pwd))

    def test_only_latin_and_digits(self):
        pwd = generate_wifi_password(8)
        self.assertTrue(re.fullmatch(r"[A-Za-z0-9]+", pwd) is not None)

    def test_too_short_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-1)

    def test_string_length(self):
        # БАГ: сейчас TypeError (str < int) вместо ValueError
        with self.assertRaises(ValueError):
            generate_wifi_password("8")

    def test_float_length(self):
        # БАГ: сейчас TypeError в range() вместо ValueError
        with self.assertRaises(ValueError):
            generate_wifi_password(8.5)

    def test_passwords_are_different(self):
        # случайность: два пароля подряд почти наверняка разные
        self.assertNotEqual(generate_wifi_password(8), generate_wifi_password(8))


# ============================================================
# 4. format_receipt — текст чека
# ============================================================
class FormatReceiptTestCase(unittest.TestCase):
    def test_receipt_contains_drink(self):
        receipt = format_receipt("latte", 1)
        self.assertIn("Напиток: latte", receipt)

    def test_receipt_contains_quantity(self):
        receipt = format_receipt("latte", 1)
        self.assertIn("Количество: 1", receipt)

    def test_receipt_contains_total(self):
        receipt = format_receipt("latte", 1)
        self.assertIn("Итого: 280 руб.", receipt)

    def test_receipt_contains_header(self):
        receipt = format_receipt("espresso", 2)
        self.assertIn("Чек Coffee", receipt)

    def test_receipt_total_calculated_correctly(self):
        receipt = format_receipt("espresso", 3)
        self.assertIn("Итого: 450 руб.", receipt)

    def test_zero_quantity_receipt(self):
        receipt = format_receipt("tea", 0)
        self.assertIn("Итого: 0 руб.", receipt)

    def test_empty_drink_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("unknown", 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_string_quantity(self):
        # БАГ: сейчас TypeError при умножении вместо ValueError
        with self.assertRaises((ValueError, TypeError)):
            format_receipt("latte", "1")

    def test_float_quantity(self):
        # БАГ: сейчас вернёт чек с "Итого: 420.0 руб."
        with self.assertRaises(ValueError):
            format_receipt("latte", 1.5)

    def test_receipt_format_regex(self):
        # Подсказка из задания: регулярное выражение
        receipt = format_receipt("latte", 2)
        pattern = r"Напиток:\s+\w+\s*\nКоличество:\s+\d+\s*\nИтого:\s+\d+\s+руб\."
        self.assertRegex(receipt, pattern)


if __name__ == "__main__":
    unittest.main()