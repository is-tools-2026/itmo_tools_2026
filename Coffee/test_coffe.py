import unittest
from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
)

class TestCoffee(unittest.TestCase):

    # Тесты для get_price
    def test_get_price_valid(self):
        self.assertEqual(get_price("espresso"), 150)
        self.assertEqual(get_price("latte"), 280)

    def test_get_price_invalid(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    # Тесты для calculate_order_total
    def test_calculate_order_total_valid(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_calculate_order_total_invalid(self):
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total(-1, 200)
        with self.assertRaises((ValueError, TypeError)):
            calculate_order_total("3", 280)

    # Тесты для get_most_expensive_drink
    def test_get_most_expensive_drink(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)

    # Тесты для generate_wifi_password
    def test_generate_wifi_password_valid(self):
        pwd = generate_wifi_password(10)
        self.assertEqual(len(pwd), 10)

    def test_generate_wifi_password_invalid(self):
        with self.assertRaises(TypeError):
            generate_wifi_password("10")

    # Тесты для format_receipt
    def test_format_receipt_valid(self):
        receipt = format_receipt("espresso", 2)
        self.assertIn("espresso", receipt)

    def test_format_receipt_invalid(self):
        with self.assertRaises(ValueError):
            format_receipt("espresso", 0)
        with self.assertRaises(ValueError):
            format_receipt("espresso", -1)

if __name__ == '__main__':
    unittest.main()