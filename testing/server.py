"""
Сервер вузовской кофейни «CampusCoffee».

Оборачивает 4 функции из Coffee/coffee.py в REST API:

    1. POST /api/order-total     -> calculate_order_total(quantity, price)
    2. GET  /api/most-expensive  -> get_most_expensive_drink()
    3. GET  /api/wifi-password   -> generate_wifi_password(length=8)
    4. POST /api/receipt         -> format_receipt(drink_name, quantity)

Запуск:
    pip install -r requirements.txt
    python server.py
"""

import sys
from pathlib import Path

from flask import Flask, jsonify, request

# Добавляем папку Coffee в sys.path, чтобы импортировать coffee.py
COFFEE_DIR = Path(__file__).resolve().parent.parent / "Coffee"
sys.path.append(str(COFFEE_DIR))

from coffee import (  # noqa: E402
    calculate_order_total,
    format_receipt,
    generate_wifi_password,
    get_most_expensive_drink,
)

app = Flask(__name__)


def read_json_object():
    """Принимает JSON-объект, остальные тела запроса отклоняет."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        raise ValueError("Тело запроса должно быть корректным JSON-объектом")
    return data


# ============================================================
# Эндпоинт 1. Стоимость заказа -> calculate_order_total
# ============================================================

@app.route("/api/order-total", methods=["POST"])
def order_total():
    """
    Вычисляет стоимость заказа.

    Тело запроса (JSON):
        {"quantity": 3, "price": 280}

    Ответ:
        {"quantity": 3, "price": 280, "total": 840}
    """
    try:
        data = read_json_object()
        quantity = data["quantity"]
        price = data["price"]
        total = calculate_order_total(quantity, price)
    except KeyError:
        return jsonify({"error": "Нужны поля quantity и price"}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify({"quantity": quantity, "price": price, "total": total})


# ============================================================
# Эндпоинт 2. Самый дорогой напиток -> get_most_expensive_drink
# ============================================================

@app.route("/api/most-expensive", methods=["GET"])
def most_expensive():
    """
    Возвращает самый дорогой напиток в меню.

    Ответ:
        {"drink": "latte", "price": 280}
    """
    try:
        name, price = get_most_expensive_drink()
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"drink": name, "price": price})


# ============================================================
# Эндпоинт 3. Пароль от Wi-Fi -> generate_wifi_password
# ============================================================

@app.route("/api/wifi-password", methods=["GET"])
def wifi_password():
    """
    Генерирует пароль от Wi-Fi кофейни.

    Query-параметр:
        length (int, необязательный, по умолчанию 8)

    Ответ:
        {"length": 8, "password": "aB3kLm9x"}
    """
    try:
        length = int(request.args.get("length", "8"))
    except ValueError:
        return jsonify({"error": "length должен быть целым числом"}), 400
    try:
        password = generate_wifi_password(length)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify({"length": length, "password": password})


# ============================================================
# Эндпоинт 4. Чек -> format_receipt
# ============================================================

@app.route("/api/receipt", methods=["POST"])
def receipt():
    """
    Формирует текст чека.

    Тело запроса (JSON):
        {"drink_name": "latte", "quantity": 2}

    Ответ:
        {"receipt": "Чек CampusCoffee\\nНапиток: latte\\n..."}
    """
    try:
        data = read_json_object()
        drink_name = data["drink_name"]
        quantity = data["quantity"]
        text = format_receipt(drink_name, quantity)
    except KeyError:
        return jsonify({"error": "Нужны поля drink_name и quantity"}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify({"receipt": text})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
