import unittest
from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)


class TestCoffeeFunctions(unittest.TestCase):

    # 1. Тесты для get_price
    def test_get_price_valid(self):
        self.assertEqual(get_price("espresso"), 150)
        self.assertEqual(get_price("latte"), 280)

    def test_get_price_invalid(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    # 2. Тесты для calculate_order_total
    def test_calculate_order_total_valid(self):
        # 2 latte * 280 = 560
        self.assertEqual(calculate_order_total("latte", 2), 560)

    def test_calculate_order_total_invalid_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total("latte", 0)
        with self.assertRaises(ValueError):
            calculate_order_total("latte", -1)

    # 3. Тесты для get_most_expensive_drink
    def test_get_most_expensive_drink(self):
    # Самый дорогой напиток в меню — latte (280)
        name, price = get_most_expensive_drink()
        self.assertEqual(name, "latte")
        self.assertEqual(price, 280)

    # 4. Тесты для generate_wifi_password
    def test_generate_wifi_password(self):
        pwd = generate_wifi_password()
        self.assertIsInstance(pwd, str)
        self.assertEqual(len(pwd), 8)

    # 5. Тесты для print_receipt
    def test_format_receipt(self):
        receipt = format_receipt("latte", 1)
        self.assertIn("---Чек Coffee---", receipt)
        self.assertIn("280", receipt)


if __name__ == "__main__":
    unittest.main()
