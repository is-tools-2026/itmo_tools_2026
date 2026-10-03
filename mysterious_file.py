# Пример


def make_tea(a, b):
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
    return f"Чай: {a} мл воды, {b} ложки сахара"


print(a(200, 2))


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


# Функция 4


def get_multiples_of_three(start, stop, step=1):
    """
    Возвращает список чисел, кратных трём, в заданном диапазоне.

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включительно)
        step (int): шаг итерации (по умолчанию 1)

    Returns:
        list[int]: список чисел, кратных 3

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
    """
    result = []
    for i in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            result.append(i)
    return result


# Функция 5


def sentiment_score(text, positive_words, negative_words):
    """
    Вычисляет оценку настроения текста на основе позитивных и негативных слов.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных слов
        negative_words (list[str]): список негативных слов

    Returns:
        float: итоговая оценка настроения (округлена до 1 знака)

    Пример:
        >>> sentiment_score("I love Python!", ["love", "like"], ["hate", "dislike"])
        1.5
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            score -= 1  # минус балл за негатив, грустно стало
        if word.endswith('!'):
            score *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))


# Функция 6


def to_binary(number):
    """
    Преобразует неотрицательное целое число в двоичную строку.

    Args:
        number (int): неотрицательное целое число

    Returns:
        str: двоичное представление числа ("0" для нуля)

    Raises:
        ValueError: если число отрицательное

    Пример:
        >>> to_binary(10)
        '1010'
        >>> to_binary(2048)
        '100000000000'
    """
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")
    if number == 0:
        return "0"
    bits = []
    while number > 0:
        bits.append(number % 2)
        number = number // 2
    bits.reverse()
    return ''.join(map(str, bits))