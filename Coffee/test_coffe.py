import unittest
from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


class TestCoffeeFunctions(unittest.TestCase):

    # 1. Тесты для get_price (3 теста)
    def test_get_price_valid(self):
        self.assertEqual(get_price("espresso"), 150)
        self.assertEqual(get_price("latte"), 280)

    def test_get_price_invalid_type(self):
        with self.assertRaises((ValueError, TypeError)):
            get_price(123)

    def test_get_price_unknown_drink(self):
        with self.assertRaises((ValueError, TypeError)):
            get_price("unknown_drink")


    # 2. Тесты для calculate_order_total (3 теста)
    def test_calculate_order_total_valid(self):
        self.assertEqual(calculate_order_total("latte", 2), 560)

    def test_calculate_order_total_zero_quantity(self):
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total("latte", 0)

    def test_calculate_order_total_negative_quantity(self):
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total("latte", -1)


    # 3. Тесты для get_most_expensive_drink (3 теста)
    def test_get_most_expensive_drink_valid(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)

    def test_get_most_expensive_drink_type(self):
        name, price = get_most_expensive_drink()
        self.assertIsInstance(name, str)
        self.assertIsInstance(price, (int, float))

    def test_get_most_expensive_drink_positive_price(self):
        _, price = get_most_expensive_drink()
        self.assertGreater(price, 0)


    # 4. Тесты для generate_wifi_password (3 теста)
    def test_generate_wifi_password_valid(self):
        pwd = generate_wifi_password()
        self.assertIsInstance(pwd, str)
        self.assertEqual(len(pwd), 8)

    def test_generate_wifi_password_uniqueness(self):
        pwd1 = generate_wifi_password()
        pwd2 = generate_wifi_password()
        self.assertNotEqual(pwd1, pwd2)

    def test_generate_wifi_password_invalid(self):
        with self.assertRaises((ValueError, TypeError)):
            generate_wifi_password(-1)


    # 5. Тесты для format_receipt (3 теста)
    def test_format_receipt_valid(self):
        receipt = format_receipt("latte", 2)
        self.assertIsInstance(receipt, str)
        self.assertIn("latte", receipt)

    def test_format_receipt_invalid_drink_type(self):
        with self.assertRaises((ValueError, TypeError)):
            format_receipt(123, 2)

    def test_format_receipt_invalid_quantity_type(self):
        with self.assertRaises((ValueError, TypeError)):
            format_receipt("latte", "two")


if __name__ == "__main__":
    unittest.main()

