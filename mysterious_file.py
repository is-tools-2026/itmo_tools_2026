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


def buy_products(money, price_per_item, items_count):
    """
    Рассчитывает сдачу после покупки товаров.

    Args:
        money (int): сумма имеющихся денег
        price_per_item (int): цена одного товара
        items_count (int): количество приобретаемых товаров

    Returns:
        int | str: сумма сдачи или сообщение о нехватке денег

    Пример:
        >>> buy_products(100, 10, 5)
        50
        >>> buy_products(20, 10, 3)
        'Недостаточно денег'
    """
    total_price = price_per_item * items_count

    if total_price > money:
        return "Недостаточно денег"

    return money - total_price


print(buy_products(100, 10, 5))


# Функция 2

def check_weekend(day):
    """
    Проверяет, является ли указанный день недели выходным.

    Args:
        day (str): название дня недели.
            Поддерживаются "сб", "вс", "суббота", "воскресенье"

    Returns:
        bool: True, если день является выходным,
        иначе False

    Пример:
        >>> check_weekend("Суббота")
        True
        >>> check_weekend("понедельник")
        False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(check_weekend("Суббота"))


# Функция 3

def check_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): целое число для проверки

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> check_even(4)
        True
        >>> check_even(7)
        False
    """
    return number % 2 == 0


print(check_even(4))

# Функция 4

def find_numbers(start, stop, step=1):
    """
    Находит числа, кратные трём, в заданном диапазоне.

    Args:
        start (int): начало диапазона
        stop (int): конец диапазона, не включается
        step (int): шаг изменения числа, по умолчанию 1

    Returns:
        list: список чисел, кратных трём

    Пример:
        >>> find_numbers(1, 10)
        [3, 6, 9]
        >>> find_numbers(1, 10, 2)
        [3, 9]
    """
    numbers = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            numbers.append(number)

    return numbers


print(find_numbers(1, 10))

# Функция 5

def calculate_sentiment(text, positive_words, negative_words):
    """
    Оценивает эмоциональную окраску текста по заданным словам.

    Args:
        text (str): текст для анализа
        positive_words (list): список позитивных слов
        negative_words (list): список негативных слов

    Returns:
        float: итоговая оценка эмоциональной окраски текста

    Пример:
        >>> calculate_sentiment("I love Python", ["love"], ["hate"])
        1
        >>> calculate_sentiment("I hate Python", ["love"], ["hate"])
        -1
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


print(calculate_sentiment(
    "I love Python!",
    ["love", "like", "enjoy", "adore", "appreciate"],
    ["hate", "dislike", "detest", "antipathy"]
))

# Функция 6

def convert_number(number, counter=0):
    """
    Преобразует число в строку из остатков от деления на два.

    Args:
        number (int): число для преобразования
        counter (int): счётчик, по умолчанию 0

    Returns:
        str: строка из остатков или "0", если число не положительное

    Пример:
        >>> convert_number(10)
        '0101'
        >>> convert_number(0)
        '0'
    """
    results = []

    while number > 0:
        results.append(number % 2)
        number = number // 2
        counter += 1

    if counter > 10:
        results.reverse()

    return ''.join(map(str, results)) if results else "0"


print(convert_number(10))

