"""
Модуль вузовской кофейни.

"""

# Меню кофейни: название -> цена
# Любимый кофе лектора - Латте
import random
import string
import math


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
    """
    Возвращает цену напитка по его названию.

    Args:
        drink_name (str): название напитка

    Returns:
        int: цена напитка
  
    Raises:
        ValueError: если напитка нет в меню
        
    Здесь всё честно: нет напитка — нет цены.
    """
    if not isinstance(drink_name, str):
        raise TypeError("Название напитка должно быть строкой")
    if drink_name not in MENU:
        raise ValueError(f"Напиток '{drink_name}' не найден в меню")
    return MENU[drink_name]

# ============================================================
# ФУНКЦИЯ 1. Вычисляет стоимость заказа
# ============================================================

def calculate_order_total(quantity, price):
    """
    Вычисляет стоимость заказа.

    Args:
        quantity (int): количество напитков
        price (int): цена одного напитка

    Returns:
        int: итоговая стоимость
    """
    if type(quantity) is not int or type(price) not in (int, float):
        raise TypeError("Количество и цена должны быть числами")
    if isinstance(price, float) and not math.isfinite(price):
        raise ValueError("Цена должна быть конечным числом")
    if quantity < 0 or price < 0:
        raise ValueError("Количество и цена не могут быть отрицательными")
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
    if not MENU:
        raise ValueError("Меню пусто")
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
        length (int): длина пароля не меньше 8
    
    Returns:
        string: пароль от wifi

    """
    if type(length) is not int:
        raise TypeError("Длина должна быть целым числом")
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
    price = get_price(drink_name)
    if type(quantity) is not int:
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")
    
    total = calculate_order_total(quantity, price)
    
    return (
        f"Чек CampusCoffee\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб."
    ) 

