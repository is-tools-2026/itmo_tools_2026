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
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))


def calculate_change(money, price_per_item, items_count):
    """
    Считает сдачу после покупки товаров по одинаковой цене.

    Args:
        money (int): сумма денег у покупателя
        price_per_item (int): цена одного товара
        items_count (int): количество купленных товаров

    Returns:
        int или str: сдача, если денег хватает; строка "Недостаточно денег", если не хватает

    Пример:
        >>> calculate_change(100, 10, 5)
        50
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(calculate_change(100, 10, 5))


def is_weekend(day_name):
    """
    Проверяет, является ли переданный день недели выходным (регистр не важен).

    Args:
        day_name (str): название дня: "сб", "вс", "суббота" или "воскресенье"

    Returns:
        bool: True, если день выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))


