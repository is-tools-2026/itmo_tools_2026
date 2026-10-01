# Пример


def make_tea(water_ml, sugar_spoons):
    """
    Готовит чай, смешивая воду и сахар.

    Args:
        water_ml (int): объём воды в миллилитрах
        sugar_spoons (int): количество ложек сахара

    Returns:
        str: описание получившегося напитка

    Пример:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    # Рецепт одобрен диетологами, которых никто не спрашивал.
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"


print(make_tea(200, 2))


# Функция 1


def calculate_change(money, price_per_item, items_count):
    """
    Вычисляет сдачу при покупке товаров.

    Args:
        money (int | float): сумма денег у покупателя
        price_per_item (int | float): цена одного товара
        items_count (int): количество покупаемых товаров

    Returns:
        int | float | str: сумма сдачи или сообщение «Недостаточно денег»

    Пример:
        >>> calculate_change(100, 10, 5)
        50
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total


print(calculate_change(100, 10, 5))


# Функция 2


def is_weekend(day):
    """
    Проверяет, является ли указанный день выходным (суббота или воскресенье).

    Args:
        day (str): название или сокращение дня недели

    Returns:
        bool: True, если день выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    # Надо подать прошение на включение Пятницы.
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(is_weekend("Суббота"))


# Функция 3


def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): целое число для проверки

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


