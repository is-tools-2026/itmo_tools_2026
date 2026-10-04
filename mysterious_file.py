# Пример

def make_tea(water_ml, sugar_spoons): #
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
    """""
        Проверяет, хватает ли денег на покупку товаров и возвращает сдачу или сообщение о недостатке средств.
        Args:
            money (int): Сумма для покупки
            price_per_item (int): Цена за товар
            item_counts (int): Количество покупаемых товаров
        Returns:
                str: Сообщение о недостатке денег
                int: Сдача после покупки
        Пример:
            >>> buy_products(100, 10, 5)
            50
            >>> buy_products(100, 20, 6)
            'Недостаточно денег'
        """""
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция. 
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check(day):
    # Надо подать прошение на включение Пятницы.
    """""
    Проверяет, является ли переданный день выходным.
    Args:
        day (str): Название дня недели
    Retrurns:
        bool: True, если день является выходным, иначе False
    Пример:
        >>> check("Суббота")
        True
        >>> check("Понедельник")
        False
    """""
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check("Суббота"))

# Функция 3

def check(number):
    """""
    Проверяет, является ли число четным.
    Args:
        number (int): Число для проверки
    Returns:
        bool: True, если число четное, иначе False
    Пример:
        >>> check(4)
        True
        >>> check(5)
        False
    """""
    return number % 2 == 0

# Функция 4

def numbers(first, last, step=1):
    """""
    Создает список чисел от a до b(не включая) сшагом c, которые делятся на 3.
    Args:
        first (int): Начальное число
        last (int): Конечное число
        step (int): Шаг между числами, по умолчанию равен 1
        Returns:
            list: Список чисел, делящихся на 3
        Пример:
            >>> numbers(1,30)
            [3, 6, 9, 12, 15, 18, 21, 24, 27]
            >>> numbers(1,30,2)
            [3, 9, 15, 21, 27]
    """""
    r = []
    for i in range(first, last, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            r.append(i)
    return r

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """""
    Определяет настроение текста по количеству позитивных и негативных слов и учитывает восклицательные и вопросительные знаки.
    Args:
        text (str): Текст для анализа
        positive_words (list): Список позитивных слов
        negative_words (list): Список негативных слов
    Returns:
        float: Оценка настроения текста, округленная до одного знака после запятой
    Пример:
        >>> sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"])
        1.5
        >>> sentiment_score("I hate alcohol?", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"])
        -0.3
    """""
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

def int_to_binary(number, count=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    """""
    Переводит число из десятичной системы счисления в двоичную, если число состоит из 10 разрядов в двоичной системе, 
    в противном случае после перевода выводит число наоборот.
    Args:
        number (int): число в десятичной системе счисления
        count (int): счетчик разрядов
    Returns:
        str: строковое число в двоичной системе
    Пример:
        >>>int_to_binary(10)
        0101
        >>>int_to_binary(10000)
        10011100010000
    """""
    result = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если number = 0 падает, но заказчик сказал "и так сойдёт"
        result.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2  # магия. не трогать!!!
        count += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if count > 10:  # 10 взял из головы, потом поменяю (нет)
        result.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, result)) if result else "0"  # FIXME: работает — не трогай

print(int_to_binary(10))
