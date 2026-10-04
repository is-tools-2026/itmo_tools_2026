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
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"


print(make_tea(200, 2))


# Функция 1

def buy_products(money, price_per_item, items_count):
    """
    Рассчитывает сдачу после покупки заданного количества товаров.

    Args:
        money (int): количество имеющихся денег
        price_per_item (int): цена одного товара
        items_count (int): количество товаров

    Returns:
        int или str: размер сдачи или сообщение о недостатке денег

    Пример:
        buy_products(100, 10, 5)
    """
    total = price_per_item * items_count

    if total > money:
        return "Недостаточно денег"

    return money - total


print(buy_products(100, 10, 5))


# Функция 2

def is_weekend(day):
    """
    Проверяет, является ли указанный день выходным.

    Args:
        day (str): название или сокращение дня недели

    Returns:
        bool: True, если день является субботой или воскресеньем,
        иначе False

    Пример:
        is_weekend("Суббота")
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(is_weekend("Суббота"))


# Функция 3

def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): число для проверки

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        is_even(4)
    """
    return number % 2 == 0


# Функция 4

def find_multiples_of_three(start, stop, step=1):
    """
    Находит числа, кратные трём, в заданном диапазоне.

    Args:
        start (int): начало диапазона
        stop (int): конец диапазона
        step (int): шаг перебора чисел

    Returns:
        list: список чисел, кратных трём

    Пример:
        find_multiples_of_three(1, 10)
    """
    result = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            result.append(number)

    return result


# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Рассчитывает оценку эмоциональной окраски текста.

    Args:
        text (str): текст для анализа
        positive_words (list): список позитивных слов
        negative_words (list): список негативных слов

    Returns:
        float: числовая оценка эмоциональной окраски текста

    Пример:
        sentiment_score("I love Python!", ["love"], ["hate"])
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


print(
    sentiment_score(
        "I love Python!",
        ["love", "like", "enjoy", "adore", "appreciate"],
        ["hate", "dislike", "detest", "antipathy"]
    )
)


# Функция 6

def build_binary_string(number, counter=0):
    """
    Формирует строку из двоичных разрядов заданного числа.

    Args:
        number (int): число для преобразования
        counter (int): начальное значение счётчика

    Returns:
        str: строка из полученных двоичных разрядов

    Пример:
        build_binary_string(10)
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        counter += 1

    # При значении счётчика больше 10 меняет порядок разрядов.
    if counter > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(build_binary_string(10))