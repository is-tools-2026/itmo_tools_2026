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
        money (int): количество денег покупателя.
        price_per_item (int): цена одного товара.
        items_count (int): количество товаров.

    Returns:
        int | str: сдача или сообщение о недостатке денег.

    Example:
        buy_products(100, 10, 5)
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def weekend(day):
    '''
    Функция проверяет является ли день выходным

    Args:
        название дня недели.

    Returns:
        True, если день является субботой или воскресеньем,
        иначе False.
    Example:
        weekend("Суббота")
    '''

    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(weekend("Суббота"))

# Функция 3

def parity(number):
    """
    Проверяет, является ли число чётным.

    Args:
         число для проверки.

    Returns:
        True, если число чётное, иначе False.
    
    Example:
        parity(10)
    """
    return number % 2 == 0

# Функция 4

def division_3(start, stop, step=1):
    """
    Находит числа, которые делятся на 3 без остатка.

    Args:
        start : начало диапазона.
        stop : конец диапазона.
        step : шаг.

    Returns:
        список чисел, кратных 3.

    Example:
        division_3(1, 10)
    """
    arr = []
    for number in range(start, stop, step):
        if number % 3 == 0:
            arr.append(number)
    return arr

# Функция 5

def sentiment_score(text, positive_word, negative_word):
    """
    Рассчитывает оценку текста.

    Args:
        text (str): текст для анализа.
        positive_words (list): список положительных слов.
        negative_words (list): список отрицательных слов.

    Returns:
        оценка тональности текста.
    Example:
        sentiment_score(
            "Это хороший день!",
            ["хороший"],
            ["плохой"]
        )
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_word:
            score += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_word:
            score -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            score *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def process_number(number, count=0):# TODO: переименовать, Витя опять не согласовал нейминг
  """
    Обрабатывает число и возвращает последовательность остатков
    от деления числа на 2.

    Args:
        number : число для обработки.
        count : количество итераций.

    Returns:
        строка с результатами обработки.
    
    Example:
        process_number(10)
    """
    digits = []  # тут будет результат, но я не уверен
  
    while number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        digits.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2  # магия. не трогать!!!
        count += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if count > 10:  # 10 взял из головы, потом поменяю (нет)
        digits.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, digits)) if digits else "0"  # FIXME: работает — не трогай

print(process_number(10))
