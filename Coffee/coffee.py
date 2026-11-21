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
    """
    Возвращает цену напитка по его названию.

    Raises:
        ValueError: если напитка нет в меню или название не строка
    """
    if not isinstance(drink_name, str):
        raise ValueError("Название напитка должно быть строкой")
    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]


def calculate_order_total(quantity, price):
    """
    Вычисляет стоимость заказа.

    Raises:
        TypeError: если quantity не целое или price не число
        ValueError: если quantity или price отрицательные
    """
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    return quantity * price


def get_most_expensive_drink():
    """
    Возвращает самый дорогой напиток в меню.

    Returns:
        tuple: (название, цена)
    """
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi: латинские буквы и цифры,
    минимум одна заглавная, одна строчная и одна цифра.

    Args:
        length (int): длина пароля (не меньше 8)

    Raises:
        TypeError: если length не целое число
        ValueError: если length меньше 8
    """
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Длина пароля должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = ''.join(random.choice(all_chars) for _ in range(length - 3))

    password_list = list(lowercase + uppercase + digit + remaining)
    random.shuffle(password_list)
    return ''.join(password_list)


def format_receipt(drink_name, quantity):
    """
    Формирует текст чека.

    Формат:
        Чек CampusCoffee
        Напиток: <название>
        Количество: <число>
        Итого: <число> руб.

    Args:
        drink_name (str): название напитка
        quantity (int): количество

    Returns:
        str: текст чека
    """
    if not isinstance(drink_name, str) or not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")

    total = get_price(drink_name) * quantity

    return (
        f"Чек CampusCoffee\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )


if __name__ == "__main__":
    print(get_price('latte'))
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt('latte', 1))
