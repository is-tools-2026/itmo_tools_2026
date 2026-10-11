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
    Проверяет, достаточно ли денег на продукты.

    Args:
        money (int): кол-во ваших денег
        price_per_item (int): Стоимость одного предмета
        items_count (int): кол-во предметов

    Returns:
        int / str: Сдачу или оповещение о нехватке денег

    Пример:
        >>> buy_products(100, 10, 5)
        50
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check(day):
    """
    Проверяет, выходной ли сегодняшний день

    Args:
        day (str): День недели, сокращение или полная версия

    Returns:
        bool: True/False - Выходной или нет

    Пример:
        >>> check("Суббота")
        True
    """
    # Надо подать прошение на включение Пятницы. 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check("Суббота"))

# Функция 3

def isEven(number):
    """
    Проверяет, делится ли число на 2

    Args:
        number (int): Любое число
    
    Returns:
        bool: True/False - делиться или нет

    Пример:
        >>> isEven(2)
        True
    """
    return number % 2 == 0

# Функция 4

def divByThree(start, end, step = 1):
    """
    Находит все числа, деляющиеся на 3 на данном отрезке

    Args:
        start (int): Начальное число диапазона
        end (int): Конечное число диапазона
        step (int): Шаг, всегда 1
    
    Returns:
        r (list): список всех чисел, делящихся на 3 на заданном диапазоне

    Пример:
        >>> divByThree(0, 10, 1)
        [0, 3, 6, 9]
    """
    r = []
    for i in range(a, b, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            r.append(i)
    return r

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Считает очки настроения полученного текста

    Args:
        text (str): Всё сообщение, которое требуется проверить
        positive_words (list with str): Список позитивных слов
        negative_words (list with str): Список отрицательных слов

    Returns:
        s (int): Счёт настроения текста

    Пример:
        >>> sentiment_score("I hate that pineapple!", ["love", "adore", "like", "enjoy"], ["hate", "dislike", "disdain", "pineapple"])
        -3
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    s = 0
    
    for word in words:
        if word in positive_words:
            s += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            s -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            s *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            s *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(s, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def binaryTransform(decimal_number, counter=0):
    """
    Возвращает строковое двоичное значение числа десятичной системы исчисления

    Args:
        decimal_number (int): Десятичное число
        counter (int): Счётчик (=0 сначала)

    Returns:
        str: Двоичная версия числа

    Пример:
        >>> binaryTransform(5, 0)
        "101"
    """
    result = []
    
    while decimal_number > 0:
        result.append(decimal_number % 2)
        decimal_number //= 2
        counter += 1
        if counter > 10:
            result.reverse()
    return ''.join(map(str, result)) if result else "0"

print(binaryTransform(10))
