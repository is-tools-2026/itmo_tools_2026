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

def buy_products(balance, price_per_item, items_count):
    """
    Проверяет возможность покупки товаров и рассчитывает остаток баланса.

    Args:
        balance (float): текущий баланс покупателя.
        price_per_item (float): цена одного товара.
        items_count (int): количество покупаемых товаров.

    Returns:
        float: остаток баланса после покупки.
        str: сообщение о недостатке средств, если денег не хватает.
    """
    total = price_per_item * items_count
    if total > balance:
        return "Недостаточно денег"
    return balance - total

print(buy_products(100, 10, 5))


# Функция 2

def is_weekend(day):
    """
    Проверяет, является ли указанный день выходным.

    Args:
        day (str): название или сокращённое обозначение дня недели.

    Returns:
        bool: True, если день является субботой или воскресеньем,
        иначе False.
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))
# Функция 3

def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): число для проверки.

    Returns:
        bool: True, если число чётное, иначе False.
    """
    return number % 2 == 0

# Функция 4

def find_multiples_of_three(start, stop, step=1):
    """
    Находит числа, кратные трём, в заданном диапазоне.

    Args:
        start (int): начало диапазона.
        stop (int): конец диапазона, не включая его.
        step (int): шаг перебора чисел.

    Returns:
        list: список чисел из диапазона, кратных трём.
    """
    result = []
    for number in range(start, stop, step):
        if number % 3 == 0:
            result.append(number)
    return result

# Функция 5

def calculate_sentiment_score(text, positive_words, negative_words):
    """
    Вычисляет оценку тональности текста на основе позитивных и негативных слов.

    Args:
        text (str): текст для анализа.
        positive_words (list): список позитивных слов.
        negative_words (list): список негативных слов.

    Returns:
        float: числовая оценка тональности текста.
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

def convert_to_binary(number, counter=0):
    """
    Переводит целое число в двоичную строку.

    Args:
        number (int): число, которое необходимо перевести в двоичную систему.
        counter (int): дополнительный счётчик итераций алгоритма.

    Returns:
        str: двоичное представление числа.
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        counter += 1

    if counter > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(convert_to_binary(10))