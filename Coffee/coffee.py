
"""
Модуль вузовской кофейни.

Содержит функции для работы с меню, заказами, скидками и бонусами.
"""

import random
import string


MENU = {
    "espresso": 150,
    "capuccino": 250,
    "latte": 280,
    "americano": 200,
    "tea": 120,
    "hot_chocolate": 220,
}

DISCOUNTS = {
    "STUDENT10": 10,
    "TEACHER15": 15,
    "HAPPY_HOUR": 20,
    "FIRST_ORDER": 5,
}


def get_price(drink_name):
    """Возвращает цену напитка по его названию."""
    if not isinstance(drink_name, str) or drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]


def calculate_order_total(quantity, price):
    """Вычисляет стоимость заказа."""
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise ValueError("Количество должно быть целым числом")
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise ValueError("Цена должна быть числом")
    if quantity < 0 or price < 0:
        raise ValueError("Количество и цена не могут быть отрицательными")
    return quantity * price


def get_most_expensive_drink():
    """Возвращает самый дорогой напиток в меню."""
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


def generate_wifi_password(length=8):
    """Генерирует пароль Wi-Fi заданной длины."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError("Длина пароля должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = ''.join(
        random.choice(all_chars) for _ in range(length - 3)
    )

    password = lowercase + uppercase + digit + remaining
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)


def format_receipt(drink_name, quantity):
    """Формирует текст чека."""
    if not isinstance(drink_name, str) or not drink_name:
        raise ValueError("Название напитка должно быть непустой строкой")

    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")

    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise ValueError("Количество должно быть целым числом")

    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")

    total = get_price(drink_name) * quantity

    return (
        f"\n---Чек Coffee---\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )
