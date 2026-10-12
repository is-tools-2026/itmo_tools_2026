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
        money (float): количество имеющихся денег.
        price_per_item (float): цена за одну единицу товара.
        items_count (int): количество единиц товара.

    Returns:
        float: сумма сдачи, если денег достаточно.
        str: сообщение "Недостаточно денег", если сумма покупки превышает деньги.

    Пример:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(30, 10, 5)
        'Недостаточно денег'
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def is_weekend(day):
    """
    Определяет, является ли день недели выходным.

    Args:
        day (str): название дня недели (например, "Суббота", "вс").

    Returns:
        bool: True, если день — суббота или воскресенье, иначе False.

    Пример:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("Понедельник")
        False
    """
    # Надо подать прошение на включение Пятницы. 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): целое число.

    Returns:
        bool: True, если число чётное, иначе False.

    Пример:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return number % 2 == 0

# Функция 4

def get_multiples_of_three(start, end, step=1):
     """
    Возвращает список чисел, кратных 3, в заданном диапазоне.

    Args:
        start (int): начало диапазона.
        end (int): конец диапазона (не включается).
        step (int, optional): шаг перебора. По умолчанию 1.

    Returns:
        list[int]: список чисел, которые делятся на 3 без остатка.

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
        >>> get_multiples_of_three(0, 20, 2)
        [0, 6, 12, 18]
    """
    result = []
    for i in range(start, end, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            result.append(i)
    return result

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Вычисляет оценку тональности текста на основе позитивных и негативных слов.

    Args:
        text (str): анализируемый текст.
        positive_words (list[str]): список слов с положительной интонацией.
        negative_words (list[str]): список слов с отрицательной интонацией.

    Returns:
        float: оценка тональности, округлённая до одного знака.

    Пример:
        >>> analyze_sentiment("I love Python!", ["love", "like"], ["hate"])
        1.5
        >>> analyze_sentiment("I hate it?", ["love"], ["hate"])
        -0.3
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

def to_binary_string(number, counter=0):
    """
    Преобразует целое число в его двоичное представление в виде строки.

    Args:
        number (int): число для преобразования.
        counter (int, optional): начальное значение счётчика итераций. По умолчанию 0.

    Returns:
        str: двоичная строка числа.

    Пример:
        >>> to_binary_string(10)
        '1010'
        >>> to_binary_string(0)
        '0'
    """
    bits = []
    while number > 0:
        bits.append(number % 2)
        number = number // 2
        counter += 1
    if counter > 10:
        bits.reverse()
    return ''.join(map(str, bits)) if bits else "0"
