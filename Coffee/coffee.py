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


# ============================================================
# ПРИМЕР. Цена напитка 
# ============================================================

def get_price(drink_name):
    """Возвращает цену; при неверном названии вызывает ValueError."""
    if not isinstance(drink_name, str):
        raise ValueError("Название напитка должно быть строкой")

    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")

    return MENU[drink_name]
# ============================================================
# ФУНКЦИЯ 1. Вычисляет стоимость заказа
# ============================================================

def calculate_order_total(quantity, price):
    """Считает сумму для целых неотрицательных количества и цены."""
    if type(quantity) is not int or quantity < 0:
        raise ValueError(
            "Количество должно быть целым неотрицательным числом"
        )

    if type(price) is not int or price < 0:
        raise ValueError(
            "Цена должна быть целым неотрицательным числом"
        )

    return quantity * price

# ============================================================
# ФУНКЦИЯ 2. Возвращает самый дорогой напиток в мен
# ============================================================

def get_most_expensive_drink():
    """
    Возвращает самый дорогой напиток в меню.

    Returns:
        tuple: (название, цена)
    """
    name = max(MENU, key=MENU.get)
    return name, MENU[name]

# ============================================================
# ФУНКЦИЯ 3. Генерация пароля от wifi
# ============================================================

def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi кофейни. Условие: длина 8 символов,
    может состоять только из латинских букв и цифр, 
    минимум одна заглавная буква, 
    минимум одна строчная буква, 
    минимум одна цифра.  
    
    Args:
        lenght (int): длина пароля
    
    Returns:
        string: пароль от wifi

    """
    if type(length) is not int:
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
# ФУНКЦИЯ 4. Вывод чека 
# ============================================================

def format_receipt(drink_name, quantity):
    """Возвращает текст чека."""

    # Получаем цену и считаем сумму.
    price = get_price(drink_name)
    total = calculate_order_total(quantity, price)

    # Возвращаем готовый чек.
    return (
        "Чек CampusCoffee\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )
