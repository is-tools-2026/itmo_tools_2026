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
    Рассчитывает сдачу после покупки товаров.

    Args:
        money (int | float): количество денег у покупателя.
        price_per_item (int | float): цена одного товара.
        items_count (int): количество товаров.

    Returns:
        int | float | str: сдача или сообщение о недостатке денег.
    
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
    Проверяет, является ли день выходным.

    Args:
        day(str): название дня недели.

    Returns:
        bool: True, если день является субботой или воскресеньем, иначе False.
    
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
        number(int): целое число для проверки.

    Returns:
        bool: True, если число чётное, иначе False.
    
    Пример:
        >>> is_even(10)
        True
    """
    return number % 2 == 0

# Функция 4

def get_multiples_of_three(start, end, step=1):
    """
    Возвращает числа, кратные трём, в заданном диапазоне.

    Args:
        start(int): начало диапазона.
        end(int): конец диапазона.
        step(int): шаг перебора чисел.

    Returns:
        list[int]: список чисел, которые делятся на три без остатка.

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
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
    Опредеяет настроение текста.

    Args:
        text(str): текст для анализа.
        positive_words(list[str]): список позитивных слов.
        negative_words(list[str]): список негативных слов.

    Returns:
        float: оценка настроения текста.
    
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
            score *= 1.5 # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(score, 1)
print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def to_binary(number, counter=0):
    """
    Переводит число в двоичную систему счисления.

    Args:
        number(int): целое число для перевода.
        counter(int): счётчик итераций

    Returns:
        str: двоичное представление числа в виде строки.

    Пример:
        >>> to_binary(10)
        '0101'
    """
    bits = []
    
    while number > 0:
        bits.append(number % 2)
        number = number // 2
        counter += 1
        if counter > 10:
            bits.reverse()
    return ''.join(map(str, bits)) if bits else "0"
print(to_binary(10))

