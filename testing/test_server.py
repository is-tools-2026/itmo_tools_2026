"""
Тесты для эндпоинтов сервера кофейни (testing/server.py).

Покрывают все 4 эндпоинта:
    1. POST /api/order-total     -> calculate_order_total
    2. GET  /api/most-expensive  -> get_most_expensive_drink
    3. GET  /api/wifi-password   -> generate_wifi_password
    4. POST /api/receipt         -> format_receipt

Запуск (из папки testing):
    python -m unittest test_server -v
"""

import string
import sys
import unittest
from pathlib import Path

# Добавляем папку testing в sys.path, чтобы импортировать server.py
sys.path.insert(0, str(Path(__file__).resolve().parent))

from server import app  # noqa: E402


class OrderTotalTestCase(unittest.TestCase):
    """Тесты для POST /api/order-total."""

    def setUp(self):
        self.client = app.test_client()

    def test_order_total_success(self):
        """Корректный расчёт стоимости заказа."""
        response = self.client.post(
            "/api/order-total",
            json={"quantity": 3, "price": 280},
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["total"], 840)

    def test_order_total_zero_quantity(self):
        """Нулевое количество -> нулевая стоимость."""
        response = self.client.post(
            "/api/order-total",
            json={"quantity": 0, "price": 280},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["total"], 0)

    def test_order_total_missing_field(self):
        """Отсутствует поле price -> 400."""
        response = self.client.post(
            "/api/order-total",
            json={"quantity": 3},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_order_total_invalid_type(self):
        """quantity не число -> 400."""
        response = self.client.post(
            "/api/order-total",
            json={"quantity": "abc", "price": 280},
        )
        self.assertEqual(response.status_code, 400)

    def test_order_total_empty_body(self):
        """Пустое тело запроса -> 400."""
        response = self.client.post("/api/order-total", json={})
        self.assertEqual(response.status_code, 400)


class MostExpensiveTestCase(unittest.TestCase):
    """Тесты для GET /api/most-expensive."""

    def setUp(self):
        self.client = app.test_client()

    def test_most_expensive_success(self):
        """Самый дорогой напиток в меню — latte за 280 руб."""
        response = self.client.get("/api/most-expensive")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["drink"], "latte")
        self.assertEqual(data["price"], 280)


class WifiPasswordTestCase(unittest.TestCase):
    """Тесты для GET /api/wifi-password."""

    def setUp(self):
        self.client = app.test_client()

    def test_wifi_password_default_length(self):
        """По умолчанию генерируется пароль длиной 8."""
        response = self.client.get("/api/wifi-password")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["length"], 8)
        self.assertEqual(len(data["password"]), 8)

    def test_wifi_password_custom_length(self):
        """Параметр length задаёт длину пароля."""
        response = self.client.get("/api/wifi-password?length=12")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["length"], 12)
        self.assertEqual(len(data["password"]), 12)

    def test_wifi_password_contains_required_chars(self):
        """Пароль содержит минимум одну заглавную, одну строчную и одну цифру."""
        response = self.client.get("/api/wifi-password?length=10")
        self.assertEqual(response.status_code, 200)
        password = response.get_json()["password"]

        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))

    def test_wifi_password_only_alnum(self):
        """Пароль состоит только из латинских букв и цифр."""
        response = self.client.get("/api/wifi-password")
        self.assertEqual(response.status_code, 200)
        password = response.get_json()["password"]
        allowed = string.ascii_letters + string.digits
        self.assertTrue(all(c in allowed for c in password))

    def test_wifi_password_too_short(self):
        """Длина меньше 8 -> 400 с сообщением об ошибке."""
        response = self.client.get("/api/wifi-password?length=5")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())


class ReceiptTestCase(unittest.TestCase):
    """Тесты для POST /api/receipt."""

    def setUp(self):
        self.client = app.test_client()

    def test_receipt_success(self):
        """Чек содержит название, количество и итоговую сумму."""
        response = self.client.post(
            "/api/receipt",
            json={"drink_name": "latte", "quantity": 2},
        )
        self.assertEqual(response.status_code, 200)
        receipt = response.get_json()["receipt"]

        self.assertIn("Напиток: latte", receipt)
        self.assertIn("Количество: 2", receipt)
        self.assertIn("Итого: 560 руб.", receipt)

    def test_receipt_unknown_drink(self):
        """Неизвестный напиток -> 400."""
        response = self.client.post(
            "/api/receipt",
            json={"drink_name": "margarita", "quantity": 1},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_receipt_negative_quantity(self):
        """Отрицательное количество -> 400."""
        response = self.client.post(
            "/api/receipt",
            json={"drink_name": "latte", "quantity": -1},
        )
        self.assertEqual(response.status_code, 400)

    def test_receipt_missing_quantity(self):
        """Отсутствует quantity -> 400."""
        response = self.client.post(
            "/api/receipt",
            json={"drink_name": "latte"},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()