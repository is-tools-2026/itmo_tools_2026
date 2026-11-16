"""
Модуль вузовской кофейни.
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
        TypeError: если название напитка не является строкой
        ValueError: если строка пустая или напитка нет в меню
    """
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")

    normalized_name = drink_name.strip().lower()
    if not normalized_name:
        raise ValueError("Название напитка не может быть пустым")
    if normalized_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")

    return MENU[normalized_name]


# ============================================================
# ФУНКЦИЯ 1. Вычисляет стоимость заказа
# ============================================================

def calculate_order_total(quantity, price):
    """
    Вычисляет стоимость заказа.

    Args:
        quantity (int): количество напитков
        price (int | float): цена одного напитка

    Returns:
        int | float: итоговая стоимость
    """
    if (
        isinstance(quantity, bool)
        or isinstance(price, bool)
        or not isinstance(quantity, int)
        or not isinstance(price, (int, float))
    ):
        raise TypeError("Количество должно быть целым числом, а цена - числом")

    if quantity <= 0 or price <= 0:
        raise ValueError("Количество и цена должны быть больше нуля")

    return round(quantity * price, 2)


# ============================================================
# ФУНКЦИЯ 2. Возвращает самый дорогой напиток в меню
# ============================================================

def get_most_expensive_drink():
    """
    Возвращает самый дорогой напиток в меню.

    Returns:
        tuple: (название, цена)
    """
    if not MENU:
        raise ValueError("Меню кофейни пусто")
    name = max(MENU, key=MENU.get)
    return name, MENU[name]


# ============================================================
# ФУНКЦИЯ 3. Генерация пароля от wifi
# ============================================================

def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi кофейни.
    Длина не менее 8 символов, латинские буквы и цифры,
    минимум одна заглавная, одна строчная буква и одна цифра.

    Args:
        length (int): длина пароля

    Returns:
        str: пароль от wifi
    """
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("Длина пароля должна быть целым числом")
    if length < 8 or length > 64:
        raise ValueError("Длина пароля должна быть от 8 до 64 символов")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = "".join(random.choice(all_chars) for _ in range(length - 3))

    password_list = list(lowercase + uppercase + digit + remaining)
    random.shuffle(password_list)
    return "".join(password_list)


# ============================================================
# ФУНКЦИЯ 4. Вывод чека
# ============================================================

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
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")

    price = get_price(drink_name)
    normalized_name = drink_name.strip().lower()
    total = calculate_order_total(quantity, price)

    return (
        f"Чек CampusCoffee\n"
        f"Напиток: {normalized_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб."
    )


# ============================================================
# ФУНКЦИЯ 5. Применение промокода на скидку
# ============================================================

def apply_discount(total, discount_code):
    """
    Применяет процентную скидку из словаря DISCOUNTS к сумме заказа.

    Args:
        total (int | float): исходная сумма заказа
        discount_code (str): промокод из словаря DISCOUNTS

    Returns:
        float: итоговая сумма со скидкой
    """
    if isinstance(total, bool) or not isinstance(total, (int, float)):
        raise TypeError("Сумма заказа должна быть числом")
    if not isinstance(discount_code, str):
        raise TypeError("Промокод должен быть строкой")
    if total <= 0:
        raise ValueError("Сумма заказа должна быть больше нуля")

    code = discount_code.strip().upper()
    if code not in DISCOUNTS:
        raise ValueError(f"Промокод '{discount_code}' недействителен")

    discount_percent = DISCOUNTS[code]
    return round(total * (1 - discount_percent / 100.0), 2)