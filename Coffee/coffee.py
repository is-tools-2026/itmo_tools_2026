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
    name = min(MENU, key=MENU.get)
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
        total (int): итоговая сумма

    Returns:
        str: текст чека
    """
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
            raise ValueError("Напитка нет в меню")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")
    
    total = get_price(drink_name) * quantity
    
    return (
        f"\n---Чек Coffee---\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    ) # Подсказка: для теста подойдет регулярное выражение

print(get_price('latte'))
print(calculate_order_total('latte', 5))
print(get_most_expensive_drink())
print(generate_wifi_password(8))
print(format_receipt('latte', 1))
