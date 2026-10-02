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


def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): проверяемое целое число

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> is_even(10)
        True
    """
    return number % 2 == 0

print(is_even(10))


def multiples_of_three_in_range(start, stop, step=1):
    """
    Перебирает числа от start до stop (не включая stop) с шагом step
    и оставляет только те, что делятся на 3.

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включая)
        step (int): шаг перебора, по умолчанию 1

    Returns:
        list: числа из диапазона, кратные трём

    Пример:
        >>> multiples_of_three_in_range(1, 10)
        [3, 6, 9]
    """
    result = []
    for number in range(start, stop, step):
        if number % 3 == 0:
            result.append(number)
    return result

print(multiples_of_three_in_range(1, 10))


def sentiment_score(text, positive_words, negative_words):
    """
    Оценивает настроение текста: +1 за позитивное слово, -1 за негативное.
    Слово, оканчивающееся на "!", умножает накопленный счёт на 1.5,
    а на "?" - на 0.3.

    Args:
        text (str): анализируемый текст
        positive_words (list): список слов, повышающих оценку
        negative_words (list): список слов, понижающих оценку

    Returns:
        float: итоговая оценка, округлённая до одного знака

    Пример:
        >>> sentiment_score("I love Python!", ["love"], ["hate"])
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

print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

