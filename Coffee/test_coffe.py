import unittest
import coffee
from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
    MENU,
    DISCOUNTS,
)


class TestCoffee(unittest.TestCase):

    # 1. Тесты для функции get_price
    def test_get_price_valid(self):
        self.assertEqual(get_price("espresso"), 150)
        self.assertEqual(get_price("latte"), 280)
        self.assertEqual(get_price("tea"), 120)

    def test_get_price_case_and_spaces(self):
        # Проверка обработки пробелов по краям и заглавных букв
        self.assertEqual(get_price("  Latte "), 280)
        self.assertEqual(get_price("ESPRESSO"), 150)

    def test_get_price_unknown_and_empty(self):
        with self.assertRaises(ValueError):
            get_price("raf_coffee")
        with self.assertRaises(ValueError):
            get_price("")
        with self.assertRaises(ValueError):
            get_price("   ")

    def test_get_price_invalid_type(self):
        # Передача нестроковых значений должна вызывать TypeError
        with self.assertRaises(TypeError):
            get_price(123)
        with self.assertRaises(TypeError):
            get_price(None)
        with self.assertRaises(TypeError):
            get_price(["latte"])

    # 2. Тесты для функции calculate_order_total
    def test_calculate_total_valid(self):
        self.assertEqual(calculate_order_total(1, 150), 150)
        self.assertEqual(calculate_order_total(3, 250), 750)
        self.assertAlmostEqual(calculate_order_total(2, 199.99), 399.98, places=2)

    def test_calculate_total_zero_and_negative(self):
        # Количество напитков и цена должны быть строго больше нуля
        with self.assertRaises(ValueError):
            calculate_order_total(0, 150)
        with self.assertRaises(ValueError):
            calculate_order_total(2, 0)
        with self.assertRaises(ValueError):
            calculate_order_total(-2, 150)
        with self.assertRaises(ValueError):
            calculate_order_total(2, -150)

    def test_calculate_total_invalid_type(self):
        with self.assertRaises(TypeError):
            calculate_order_total("2", 150)
        with self.assertRaises(TypeError):
            calculate_order_total(2, "150")
        # В Python bool является подклассом int, но True/False недопустимы как количество
        with self.assertRaises(TypeError):
            calculate_order_total(True, 150)
        with self.assertRaises(TypeError):
            calculate_order_total(2, False)

    # 3. Тесты для функции get_most_expensive_drink
    def test_most_expensive_drink(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)
        self.assertTrue(price == max(MENU.values()))
        self.assertFalse(name == "tea")

    # 4. Тесты для функции generate_wifi_password
    def test_wifi_password_length_and_chars(self):
        pwd8 = generate_wifi_password(8)
        self.assertEqual(len(pwd8), 8)
        self.assertTrue(pwd8.isalnum())
        self.assertTrue(any(c.islower() for c in pwd8))
        self.assertTrue(any(c.isupper() for c in pwd8))
        self.assertTrue(any(c.isdigit() for c in pwd8))

    def test_wifi_password_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)
        with self.assertRaises(ValueError):
            generate_wifi_password(0)
        with self.assertRaises(ValueError):
            generate_wifi_password(-5)

    def test_wifi_password_invalid_type(self):
        with self.assertRaises(TypeError):
            generate_wifi_password("8")
        with self.assertRaises(TypeError):
            generate_wifi_password(True)

    # 5. Тесты для функции format_receipt
    def test_format_receipt_valid(self):
        receipt = format_receipt("latte", 2)
        self.assertIn("Чек CampusCoffee", receipt)
        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_format_receipt_invalid_values(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)
        with self.assertRaises(ValueError):
            format_receipt("unknown", 1)
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)
        with self.assertRaises(ValueError):
            format_receipt("latte", -3)

    def test_format_receipt_invalid_types(self):
        with self.assertRaises(TypeError):
            format_receipt(123, 2)
        with self.assertRaises(TypeError):
            format_receipt("latte", "2")
        with self.assertRaises(TypeError):
            format_receipt("latte", True)

    # 6. Тесты для функции скидок apply_discount (работа со словарем DISCOUNTS)
    def test_apply_discount_valid(self):
        self.assertTrue(
            hasattr(coffee, "apply_discount"),
            "Функция apply_discount для работы со словарем DISCOUNTS не реализована",
        )
        # 280 руб. со скидкой STUDENT10 (10%) = 252.0 руб.
        self.assertAlmostEqual(coffee.apply_discount(280, "STUDENT10"), 252.0, places=2)
        # 200 руб. со скидкой TEACHER15 (15%) = 170.0 руб.
        self.assertAlmostEqual(coffee.apply_discount(200, "TEACHER15"), 170.0, places=2)

    def test_apply_discount_invalid(self):
        self.assertTrue(
            hasattr(coffee, "apply_discount"),
            "Функция apply_discount для работы со словарем DISCOUNTS не реализована",
        )
        with self.assertRaises(ValueError):
            coffee.apply_discount(280, "FAKE_PROMO")
        with self.assertRaises(ValueError):
            coffee.apply_discount(-100, "STUDENT10")
        with self.assertRaises(TypeError):
            coffee.apply_discount("280", "STUDENT10")


if __name__ == "__main__":
    unittest.main()