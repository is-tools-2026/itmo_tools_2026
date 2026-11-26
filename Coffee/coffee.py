"""
Модуль вузовской кофейни.

Содержит функции для работы с меню, заказами, скидками и бонусами.

ВАЖНО: в одних функциях есть обработка ошибок, в других — нет.
Твоя задача — написать тесты, которые это выявят.
А потом — исправить то, что нашёл.

Удачи! Она тебе понадобится. 🍀
"""

# Меню кофейни: название -> цена
# Любимый кофе лектора - Латте
import math
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

# Скидки: код -> процент
# Скидка для преподов больше, чем для студентов.
# Это не баг, это мотивация хорошо учиться.
DISCOUNTS = {
    "STUDENT10": 10,
    "TEACHER15": 15,
    "HAPPY_HOUR": 20,
    "FIRST_ORDER": 5,
}


def _is_int(value):
    """True, если value — целое число (bool не считается: True == 1 — ловушка)."""
    return isinstance(value, int) and not isinstance(value, bool)


# ============================================================
# ПРИМЕР. Цена напитка
# ============================================================

def get_price(drink_name):
    """
    Возвращает цену напитка по его названию.

    Args:
        drink_name (str): название напитка

    Returns:
        int: цена напитка

    Raises:
        ValueError: если напитка нет в меню (в том числе если передана не строка)

    Здесь всё честно: нет напитка — нет цены.
    """
    # isinstance нужен, чтобы нехешируемые значения (например, список)
    # давали ValueError, а не TypeError из `in MENU`
    if not isinstance(drink_name, str) or drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]


# ============================================================
# ФУНКЦИЯ 1. Вычисляет стоимость заказа
# ============================================================

def calculate_order_total(quantity, price):
    """
    Вычисляет стоимость заказа.

    Args:
        quantity (int): количество напитков (целое, больше 0)
        price (int | float): цена одного напитка (конечное число, больше 0)

    Returns:
        int | float: итоговая стоимость

    Raises:
        ValueError: если quantity — не целое число больше 0
                    или price — не конечное число больше 0
    """
    if not _is_int(quantity):
        raise ValueError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("Цена должна быть числом")
    if not math.isfinite(price):
        raise ValueError("Цена должна быть конечным числом")
    if price <= 0:
        raise ValueError("Цена должна быть больше нуля")

    return quantity * price


# ============================================================
# ФУНКЦИЯ 2. Возвращает самый дорогой напиток в меню
# ============================================================

def get_most_expensive_drink():
    """
    Возвращает самый дорогой напиток в меню.

    Returns:
        tuple: (название, цена)
    """
    name = max(MENU, key=MENU.get)  # было min -> возвращался самый дешёвый
    return name, MENU[name]


# ============================================================
# ФУНКЦИЯ 3. Генерация пароля от wifi
# ============================================================

def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi кофейни. Условие: длина не меньше 8 символов
    (по умолчанию 8), может состоять только из латинских букв и цифр,
    минимум одна заглавная буква,
    минимум одна строчная буква,
    минимум одна цифра.

    Args:
        length (int): длина пароля (целое, не меньше 8)

    Returns:
        str: пароль от wifi

    Raises:
        ValueError: если length — не целое число или меньше 8
    """
    if not _is_int(length):
        raise ValueError("Длина пароля должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    rng = random.SystemRandom()  # криптостойкий генератор для паролей
    lowercase = rng.choice(string.ascii_lowercase)
    uppercase = rng.choice(string.ascii_uppercase)
    digit = rng.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = ''.join(rng.choice(all_chars) for _ in range(length - 3))

    password = lowercase + uppercase + digit + remaining
    password_list = list(password)
    rng.shuffle(password_list)
    return ''.join(password_list)


# ============================================================
# ФУНКЦИЯ 4. Вывод чека
# ============================================================

def format_receipt(drink_name, quantity):
    """
    Формирует текст чека.

    Формат:
        ---Чек Coffee---
        Напиток: <название>
        Количество: <число>
        Итого: <число> руб.

    Args:
        drink_name (str): название напитка
        quantity (int): количество (целое, больше 0)

    Returns:
        str: текст чека

    Raises:
        ValueError: если название пустое / не строка / нет в меню,
                    или количество — не целое число больше 0
    """
    if not isinstance(drink_name, str):
        raise ValueError("Название напитка должно быть строкой")
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    # get_price сам проверит тип и наличие в меню
    price = get_price(drink_name)
    # calculate_order_total проверит quantity (тип, 0, отрицательные)
    total = calculate_order_total(quantity, price)

    return (
        f"\n---Чек Coffee---\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )  # Подсказка: для теста подойдет регулярное выражение


if __name__ == "__main__":
    # демо-запуск: раньше эти print выполнялись при каждом import coffee
    print(get_price('latte'))
    print(calculate_order_total(5, get_price('latte')))
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt('latte', 1))