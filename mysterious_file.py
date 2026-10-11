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
        money (int | float): сумма денег покупателя.
        price_per_item (int | float): стоимость одного товара.
        items_count (int): количество товаров.

    Returns:
        int | float: сдача, если денег достаточно.
        str: сообщение "Недостаточно денег", если средств не хватает.

    Пример:
        >>> buy_products(100, 10, 5)
        50
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def is_weekend(day):
    """
    Проверяет, является ли указанный день недели выходным.

    Args:
        day (str): название дня недели или его сокращение
            на русском языке.

    Returns:
        bool: True, если день — суббота или воскресенье,
            иначе False.

    Пример:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("понедельник")
        False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))
    

# Функция 3

def is_even(number):
    """
    Проверяет, является ли целое число чётным.

    Args:
        number (int): целое число для проверки.

    Returns:
        bool: True, если число чётное,
            иначе False.

    Пример:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return number % 2 == 0

# Функция 4

def find_multiples_of_three(start, stop, step=1):
    """
    Возвращает список чисел, кратных трём, из заданного диапазона.

    Args:
        start (int): начальное значение диапазона.
        stop (int): конечная граница диапазона (не включается).
        step (int): шаг перебора, по умолчанию 1.
            Не должен быть равен нулю.

    Returns:
        list[int]: список чисел, делящихся на 3 без остатка.

    Пример:
        >>> find_multiples_of_three(1, 10)
        [3, 6, 9]
        >>> find_multiples_of_three(3, 15, 3)
        [3, 6, 9, 12]
    """
    multiples = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            multiples.append(number)

    return multiples

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Оценивает эмоциональную окраску текста по заданным спискам слов.

    За каждое положительное слово добавляется 1 балл,
    за каждое отрицательное вычитается 1 балл.
    Восклицательный знак в конце слова умножает текущую
    оценку на 1.5, вопросительный знак — на 0.3.

    Args:
        text (str): текст для анализа.
        positive_words (list[str]): список положительных слов.
        negative_words (list[str]): список отрицательных слов.

    Returns:
        float: итоговая оценка эмоциональной окраски текста,
            округлённая до одного знака после запятой.

    Пример:
        >>> sentiment_score("love", ["love"], ["hate"])
        1
        >>> sentiment_score("hate", ["love"], ["hate"])
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

print(sentiment_score(
    "I love Python!", ["love", "like", "enjoy", "adore", "appreciate"],
    ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def number_to_binary(number, counter=0):
    """
    Формирует строку из двоичных цифр целого числа.

    Остатки от деления числа на 2 записываются в список.
    Если итоговое значение счётчика превышает 10,
    список разворачивается перед объединением в строку.

    Особенность: если counter не превышает 10,
    цифры остаются в обратном порядке.

    Args:
        number (int): неотрицательное целое число.
        counter (int): начальное значение счётчика,
            по умолчанию 0.

    Returns:
        str: строка из двоичных цифр числа.
            Для нуля возвращается "0".

    Пример:
        >>> number_to_binary(10)
        '0101'
        >>> number_to_binary(10, 7)
        '1010'
        >>> number_to_binary(0)
        '0'
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        counter += 1

    if counter > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(number_to_binary(10))





