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
        money (int | float): Доступная сумма денег
        price_per_item (int | float): Цена за одну единицу товара
        items_count (int): Количество покупаемых единиц товара

    Returns:
        int | float: Сдача, если денег хватает
        str: "Недостаточно денег", если сумма покупки превышает доступные средства.

    Example:
        >>> buy_products(100,10, 7)
        30
        >>> buy_products(30, 10, 6)
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
    Проверяет, является ли указанный день выходным 

    Args:
        day (str): Название дня недели

    Returns:
        bool: True если день - сб или вс,иначе False

    Example:
    >>> is_weekend("Суббота")
        True
    >>> is_weekend("Среда")
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
        number (int): Число для проверки

    Returns:
        bool: True если число чётное, иначе False

    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return number % 2 == 0

# Функция 4

def find_multiples_of_three(start, stop, step=1):
    """
    Возвращает список чисел из диапазона [start, stop) с шагом step,
    которые делятся на 3 без остатка.

    Args:
        start (int): Начало диапазона (включительно).
        stop (int): Конец диапазона (не включительно).
        step (int, optional): Шаг диапазона. По умолчанию 1.

    Returns:
        list[int]: Список чисел, кратных 3.

    Example:
        >>> find_multiples_of_three(0, 10)
        [0, 3, 6, 9]
        >>> find_multiples_of_three(0, 20, 2)
        [0, 6, 12, 18]
    """
    result = []
    for i in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            result.append(i)
    return result

# Функция 5

def calculate_sentiment_score(text, positive_words, negative_words):
    """
    Оценивает эмоциональную окраску текста.

    За каждое позитивное слово начисляется +1 балл, за негативное — -1 балл.
    Если слово заканчивается на '!', итоговый балл умножается на 1.5.
    Если на '?', умножается на 0.3.

    Args:
        text (str): Анализируемый текст.
        positive_words (list[str]): Список позитивных слов.
        negative_words (list[str]): Список негативных слов.

    Returns:
        float: Оценка настроения, округлённая до одного знака после запятой.

    Example:
        >>> calculate_sentiment_score("I love Python!", ["love"], ["hate"])
        1.5
        >>> calculate_sentiment_score("I hate bugs?", ["love"], ["hate"])
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


print(calculate_sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6
def to_binary_string(number, iterations=0): # TODO: переименовать, Витя опять не согласовал нейминг
    """
    Переводит число в двоичную строку.

    Если количество итераций (iterations) превышает 10,
    строка разворачивается (инвертируется порядок битов).

    Args:
        number (int): Число для перевода в двоичную систему.
        iterations (int, optional): Начальный счётчик итераций. По умолчанию 0.

    Returns:
        str: Двоичное представление числа в виде строки.

    Example:
        >>> to_binary_string(10)
        '1010'
        >>> to_binary_string(5)
        '101'
    """
    bits = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        bits.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2 # магия. не трогать!!!
        iterations += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if iterations> 10:  # 10 взял из головы, потом поменяю (нет)
        bits.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, bits)) if bits else "0"  # FIXME: работает — не трогай

print(to_binary_string(10))
