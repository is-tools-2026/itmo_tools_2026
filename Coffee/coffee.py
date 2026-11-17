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


def _is_int(value):
    """True, если value — целое число (bool не считается числом)."""
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

    Raises:
        TypeError: если quantity или price не целые числа
        ValueError: если quantity или price отрицательные
    """
    if not _is_int(quantity):
        raise TypeError("Количество должно быть целым числом")
    if not _is_int(price):
        raise TypeError("Цена должна быть целым числом")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным")
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    return quantity * price

# ============================================================
# ФУНКЦИЯ 2. Возвращает самый дорогой напиток в меню
# ============================================================

def get_most_expensive_drink():
    """
    Возвращает самый дорогой напиток в меню.

    Returns:
        tuple: (название, цена)

    Raises:
        ValueError: если меню пустое
    """
    if not MENU:
        raise ValueError("Меню пустое")
    name = max(MENU, key=MENU.get)
    return name, MENU[name]

# ============================================================
# ФУНКЦИЯ 3. Генерация пароля от wifi
# ============================================================

def generate_wifi_password(length=8):
    """
    Генерирует пароль для Wi-Fi кофейни. Условие: длина не меньше 8 символов,
    может состоять только из латинских букв и цифр,
    минимум одна заглавная буква,
    минимум одна строчная буква,
    минимум одна цифра.

    Args:
        length (int): длина пароля

    Returns:
        str: пароль от wifi

    Raises:
        TypeError: если length не целое число
        ValueError: если length меньше 8
    """
    if not _is_int(length):
        raise TypeError("Длина пароля должна быть целым числом")
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

    Raises:
        ValueError: если название пустое, напитка нет в меню
                    или количество не положительное
        TypeError: если количество не целое число
    """
    if not drink_name:
        raise ValueError("Название напитка не может быть пустым")
    if drink_name not in MENU:
        raise ValueError("Напитка нет в меню")
    if not _is_int(quantity):
        raise TypeError("Количество должно быть целым числом")
    if quantity <= 0:
        raise ValueError("Количество должно быть больше нуля")

    total = calculate_order_total(quantity, get_price(drink_name))

    return (
        f"Чек CampusCoffee\n"
        f"Напиток: {drink_name}\n"
        f"Количество: {quantity}\n"
        f"Итого: {total} руб.\n"
    )  # Подсказка: для теста подойдет регулярное выражение


if __name__ == "__main__":
    print(get_price('latte'))
    print(calculate_order_total(5, get_price('latte')))
    print(get_most_expensive_drink())
    print(generate_wifi_password(8))
    print(format_receipt('latte', 1))