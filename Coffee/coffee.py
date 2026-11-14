"""
Модуль вузовской кофейни «CampusCoffee» (исправленная версия).

Во всех функциях некорректный ввод приводит к ValueError.
"""

import random
import string

# Меню кофейни: название -> цена
MENU = {
    "espresso": 150,
    "capuccino": 250,
    "latte": 280,
    "americano": 200,
    "tea": 120,
    "hot_chocolate": 220,
}

# Скидки: код -> процент
DISCOUNTS = {
    "STUDENT10": 10,
    "TEACHER15": 15,
    "HAPPY_HOUR": 20,
    "FIRST_ORDER": 5,
}


def _check_int(value, name, minimum=0):
    """Проверяет, что value — целое число (не bool) и value >= minimum."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} должно быть целым числом")
    if value < minimum:
        raise ValueError(f"{name} не может быть меньше {minimum}")


def _check_drink(drink_name):
    """Проверяет, что drink_name — непустая строка из меню."""
    if not isinstance(drink_name, str):
        raise ValueError("Название напитка должно быть строкой")
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")


# ============================================================
# ПРИМЕР. Цена напитка
# ============================================================

def get_price(drink_name):
    """
    Возвращает цену напитка по его названию.

    Raises:
        ValueError: если напитка нет в меню или название не строка
    """
    # БЫЛО: get_price([]) падало с TypeError (unhashable type)
    _check_drink(drink_name)
    return MENU[drink_name]


# ============================================================
# ФУНКЦИЯ 1. Стоимость заказа
# ============================================================

def calculate_order_total(quantity, price):
    """
    Вычисляет стоимость заказа.

    Args:
        quantity (int): количество напитков (>= 0)
        price (int): цена одного напитка (>= 0)

    Raises:
        ValueError: если аргументы не целые или отрицательные
    """
    # БЫЛО: return quantity * price -> ('latte', 5) давало 'lattelatte...',
    # а отрицательные значения давали отрицательную сумму
    _check_int(quantity, "Количество")
    _check_int(price, "Цена")
    return quantity * price


# ============================================================
# ФУНКЦИЯ 2. Самый дорогой напиток
# ============================================================

def get_most_expensive_drink():
    """Возвращает кортеж (название, цена) самого дорогого напитка."""
    # БЫЛО: min(...) -> возвращался самый дешёвый напиток (tea)
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


# ============================================================
# ФУНКЦИЯ 3. Пароль от Wi-Fi
# ============================================================

def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi: латинские буквы и цифры,
    минимум одна заглавная, одна строчная и одна цифра.

    Args:
        length (int): длина пароля (>= 8)

    Raises:
        ValueError: если length не целое или меньше 8
    """
    # БЫЛО: generate_wifi_password("8") / (None) падали с TypeError
    _check_int(length, "Длина пароля")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    rng = random.SystemRandom()  # криптостойкий генератор для паролей
    lowercase = rng.choice(string.ascii_lowercase)
    uppercase = rng.choice(string.ascii_uppercase)
    digit = rng.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = [rng.choice(all_chars) for _ in range(length - 3)]

    password_list = [lowercase, uppercase, digit] + remaining
    rng.shuffle(password_list)
    return "".join(password_list)


# ============================================================
# ФУНКЦИЯ 4. Чек
# ============================================================

def format_receipt(drink_name, quantity):
    """
    Формирует текст чека.

    Формат:
        ---Чек Coffee---
        Напиток: <название>
        Количество: <число>
        Итого: <число> руб.

    Raises:
        ValueError: неверное название, нет в меню, количество не целое или < 1
    """
    # БЫЛО: quantity="2" -> TypeError, drink_name=[] -> TypeError,
    # quantity=0 давало чек на 0 руб., в докстринге был лишний аргумент total
    _check_drink(drink_name)
    _check_int(quantity, "Количество", minimum=1)

    total = get_price(drink_name) * quantity

    return (
        f"\n---Чек Coffee---\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )


if __name__ == "__main__":
    # БЫЛО: print(...) на уровне модуля выполнялись при каждом import
    print(get_price("latte"))
    print(calculate_order_total(5, 280))
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt("latte", 1))
