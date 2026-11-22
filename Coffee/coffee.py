"""
Модуль вузовской кофейни.
ИСПРАВЛЕННАЯ ВЕРСИЯ (баги устранены, добавлена обработка ошибок).
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

# ============================================================
# ФУНКЦИЯ 0. Цена напитка
# ============================================================
def get_price(drink_name):
    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]

# ============================================================
# ФУНКЦИЯ 1. Стоимость заказа (ИСПРАВЛЕНО)
# ============================================================
def calculate_order_total(quantity, price):
    """Вычисляет стоимость заказа с проверкой входных данных."""
    if not isinstance(quantity, int) or not isinstance(price, int):
        raise ValueError("Количество и цена должны быть целыми числами")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    return quantity * price

# ============================================================
# ФУНКЦИЯ 2. Самый дорогой напиток (ИСПРАВЛЕНО)
# ============================================================
def get_most_expensive_drink():
    """Возвращает самый дорогой напиток в меню."""
    name = max(MENU, key=MENU.get) # было min()
    return name, MENU[name]

# ============================================================
# ФУНКЦИЯ 3. Генерация пароля (ИСПРАВЛЕНО)
# ============================================================
def generate_wifi_password(length=8):
    """Генерирует пароль для Wi-Fi кофейни."""
    if not isinstance(length, int):
        raise ValueError("Длина пароля должна быть целым числом")
    if length < 8:
        raise ValueError("Длина пароля должна быть не меньше 8 символов")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)

    all_chars = string.ascii_letters + string.digits
    remaining = ''.join(random.choice(all_chars) for _ in range(length - 3))

    password = lowercase + uppercase + digit + remaining
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# ============================================================
# ФУНКЦИЯ 4. Чек (ИСПРАВЛЕНО)
# ============================================================
def format_receipt(drink_name, quantity):
    """Формирует текст чека с проверкой данных."""
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")
    if not isinstance(quantity, int):
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

# ============================================================
# Блок для ручного запуска (убрали print при импорте)
# ============================================================
if __name__ == "__main__":
    print(get_price('latte'))
    print(calculate_order_total(5, 280)) # ИСПРАВЛЕНО: передаем числа, а не строку
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt('latte', 1))