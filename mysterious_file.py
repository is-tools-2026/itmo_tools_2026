# Пример

def make_tea(water_ml, sugar_spoons):
    """
    Готовит чай, смешивая воду и сахар.

    Args:
        water_ml (int): объём воды в миллилитрах.
        sugar_spoons (int): количество ложек сахара.

    Returns:
        str: описание получившегося напитка.

    Example:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    # Рецепт одобрен диетологами, которых никто не спрашивал.
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"


print(make_tea(200, 2))


# Функция 1

def buy_products(money, price_per_item, items_count):
    """
    Рассчитывает стоимость покупки и сдачу.

    Args:
        money (int | float): количество денег у покупателя.
        price_per_item (int | float): цена одного товара.
        items_count (int): количество покупаемых товаров.

    Returns:
        int | float | str: сдача, если денег достаточно,
        или сообщение "Недостаточно денег", если денег не хватает.

    Example:
        >>> buy_products(100, 10, 5)
        50
    """
    total_cost = price_per_item * items_count

    if total_cost > money:
        return "Недостаточно денег"

    return money - total_cost


print(buy_products(100, 10, 5))


# Функция 2

def is_weekend_day(day):
    """
    Проверяет, является ли указанный день выходным.

    Args:
        day (str): название или сокращённое название дня недели.

    Returns:
        bool: True, если день является субботой или воскресеньем,
        иначе False.

    Example:
        >>> is_weekend_day("Суббота")
        True
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(is_weekend_day("Суббота"))


# Функция 3

def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): целое число для проверки.

    Returns:
        bool: True, если число чётное, иначе False.

    Example:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


# Функция 4

def get_multiples_of_three(start, stop, step=1):
    """
    Находит числа, кратные трём, в заданном диапазоне.

    Args:
        start (int): начальное значение диапазона.
        stop (int): конечное значение диапазона.
        step (int): шаг изменения значения.

    Returns:
        list[int]: список чисел из диапазона, которые делятся на 3 без остатка.

    Example:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
    """
    multiples = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            multiples.append(number)

    return multiples


# Функция 5

def calculate_sentiment_score(text, positive_words, negative_words):
    """
    Рассчитывает оценку эмоциональной окраски текста.

    Положительные слова увеличивают оценку на 1,
    отрицательные слова уменьшают оценку на 1.
    Если слово заканчивается на "!", оценка умножается на 1.5.
    Если слово заканчивается на "?", оценка умножается на 0.3.

    Args:
        text (str): текст, эмоциональную окраску которого нужно определить.
        positive_words (list[str]): список положительных слов.
        negative_words (list[str]): список отрицательных слов.

    Returns:
        float: итоговая оценка эмоциональной окраски текста,
        округлённая до одного знака после запятой.

    Example:
        >>> calculate_sentiment_score(
        ...     "I love Python!",
        ...     ["love", "like", "enjoy", "adore", "appreciate"],
        ...     ["hate", "dislike", "detest", "antipathy"]
        ... )
        1.5
    """
    words = text.lower().split()
    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

        if word.endswith('!'):
            score *= 1.5
        elif word.endswith('?'):
            score *= 0.3

    return round(score, 1)


print(calculate_sentiment_score(
    "I love Python!",
    ["love", "like", "enjoy", "adore", "appreciate"],
    ["hate", "dislike", "detest", "antipathy"]
))


# Функция 6

def convert_to_binary(number, iteration_count=0):
    """
    Формирует строку из остатков от последовательного деления числа на 2.

    Функция последовательно получает остаток от деления числа на 2,
    добавляет его в список, а затем делит число на 2 без остатка.
    После завершения цикла список может быть перевёрнут в зависимости
    от значения счётчика итераций.

    Args:
        number (int): целое число, для которого выполняются вычисления.
        iteration_count (int): начальное значение счётчика итераций.

    Returns:
        str: строка, состоящая из полученных остатков.
        Если исходное число равно 0, возвращается "0".

    Example:
        >>> convert_to_binary(10)
        '0101'
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        iteration_count += 1

    if iteration_count > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(convert_to_binary(10))