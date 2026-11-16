"""Модуль вузовской кофейни."""

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
    """Возвращает цену напитка.

    TypeError: название не является строкой.
    ValueError: напитка нет в меню.
    """
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")
    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]


def calculate_order_total(quantity, price):
    """Возвращает стоимость заказа (int или float).

    Количество — целое число, цена — int или float.
    Значения должны быть неотрицательными. bool не допускается.
    """
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом")
    if quantity < 0 or price < 0:
        raise ValueError("Количество и цена не могут быть отрицательными")
    return quantity * price


def get_most_expensive_drink():
    """Возвращает кортеж (название, цена) самого дорогого напитка.

    ValueError: меню пустое.
    При одинаковой максимальной цене выбирается первый напиток.
    """
    if not MENU:
        raise ValueError("Меню пустое")
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


def generate_wifi_password(length=8):
    """Генерирует пароль длиной не меньше 8 символов.

    Пароль содержит только латинские буквы и цифры,
    включая минимум одну строчную букву, заглавную букву и цифру.

    TypeError: длина не является целым числом или является bool.
    ValueError: длина меньше 8.
    """
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Длина должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]

    all_chars = string.ascii_letters + string.digits
    password.extend(random.choice(all_chars) for _ in range(length - 3))
    random.shuffle(password)

    return "".join(password)


def format_receipt(drink_name, quantity):
    """Формирует текст чека.

    Формат:
        Чек CampusCoffee
        Напиток: <название>
        Количество: <число>
        Итого: <число> руб.

    Название — строка с напитком из меню.
    Количество — положительное целое число, bool не допускается.
    """
    price = get_price(drink_name)

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")

    total = calculate_order_total(quantity, price)

    return (
        "Чек CampusCoffee\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб."
    )