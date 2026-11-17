
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
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")
    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")
    return MENU[drink_name]


def calculate_order_total(quantity, price):
    if type(quantity) != int or type(price) != int:
        raise TypeError("Количество и цена должны быть целыми числами")
    if quantity < 0 or price < 0:
        raise ValueError("Количество и цена не могут быть отрицательными")
    return quantity * price


def get_most_expensive_drink():
    if len(MENU) == 0:
        raise ValueError("Меню пустое")
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


def generate_wifi_password(length=8):
    if type(length) != int:
        raise TypeError("Длина пароля должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    mal = random.choice(string.ascii_lowercase)
    bol = random.choice(string.ascii_uppercase)
    cifra = random.choice(string.digits)
    simvoly = string.ascii_letters + string.digits
    ostatok = ""

    for i in range(length - 3):
        ostatok += random.choice(simvoly)

    parol = list(mal + bol + cifra + ostatok)
    random.shuffle(parol)
    return "".join(parol)


def format_receipt(drink_name, quantity):
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")
    if type(quantity) != int:
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")

    summa = get_price(drink_name) * quantity
    return (
        f"\n---Чек CampusCoffee---\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {summa} руб.\n"
    )


if __name__ == "__main__":
    print(get_price("latte"))
    print(calculate_order_total(5, get_price("latte")))
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt("latte", 1))
