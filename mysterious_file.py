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
    Вычисляет сдачу после покупки товаров или сообщает о недостатке средств. 

    Args:
        money (float or int): сумма денег у покупателя
        price_per_item (float or int): цена за один товар
        items_count (int): количество товаров, которые хочет купить

    Returns:
        float or str or int: сдача после покупки или сообщение о недостатке средств

    Пример:
        >>> buy_products(100, 10, 5)
        50
        >>> buy_products(100, 10, 15)
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
    Проверяет, нужный день выходной или нет.

    Args:
        day (str): название или сокращение дня недели


    Returns:
        bool: True, если выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("вт")
        False

    """
    # Надо подать прошение на включение Пятницы. 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(num):
    """
    Проверяет, число на четность. Если не чет то False, если чет то True.

    Args:
        num (int): число для проверки


    Returns:
        bool: True, если чет, иначе False

    Пример:
        >>> is_even(8)
        True
        >>> is_even(3)
        False

    """

    return num % 2 == 0

# Функция 4

def get_multiples_of_three(start, end, step=1):
    """
    Возвращает список кратных трём чисел в заданном диапазоне.

    Args:
        start (int): начальное число диапазона
        end (int): конечное число диапазона
        step (int, optional): шаг между числами в диапазоне.


    Returns:
        list: списочек чисел, кратных трём
        

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]

    """
    res = []
    for num in range(start, end, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if num % 3 == 0:
            res.append(num)
    return res

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Определяет эмоциональный окрас текста, по словам из списков позитивных и негативных слов.

    Args:
        text (str): стартовый текст
        positive_words (list): список позитивных слов
        negative_words (list): список негативных слов


    Returns:
        float: рассчитанный балл настроения, округленный до одного знака
        

    Пример:
        >>> sentiment_score("Is your day good or bad?", ["good"], ["bad"])
        0.3

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

def to_binary(number, counter=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    """
    Преобразует число в двоичную систему счисления.
    Args:
        number (int): исходное целое число
        counter (int): начальное значение счетчика делений

    Returns:
        str: строковое представление числа в двоичной системе
    Пример:
        >>> to_binary(10)
        '1010'
    """ 
    bits = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        bits.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2  # магия. не трогать!!!
        counter += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if counter > 10:  # 10 взял из головы, потом поменяю (нет)
        bits.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, bits)) if bits else "0"  # FIXME: работает — не трогай

print(to_binary(10))
