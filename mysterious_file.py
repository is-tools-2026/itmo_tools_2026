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

def buy_products(money, price_per_item, items_count ):
    """
    Выдает сдачу, если денег хватает. Если нет - выводит информацию о недостатке

    Args:
        money (int/float): количество денег
        price_per_item (int/float): стоимость одного  товара
        price_per_item (int): количество покупаемых товаров 
    
    Returns:
        int/float: сдача(если денег хватает)
        str: "Недостаточно денег"(если денег не хватает)
    
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

def is_weekend(day):
    """
    Проверяет, являеется ли указанный выходным(суббота или воскресенье)

    Args:
        day(str): название дня недели (например, "Суббота", "вс")
    
    Returns:
        bool: True, если день — выходной, иначе False

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
        number (int): число для проверки

    Returns:
        bool: True, если число чётное, иначе False
    Пример:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
    """
    return number % 2 == 0

# Функция 4

def get_multiples_of_three(start, end, step=1):
    """
    Возвращает список чисел в диапазоне [start, end) с шагом step,
    которые делятся на 3 без остатка.

    Args:
        start (int): начало диапазона
        end (int): конец диапазона (не включается)
        step (int, optional): шаг перебора. По умолчанию 1.

    Returns:
        list: список чисел, делящихся на 3

    Пример:
        >>> get_multiples_of_three(1, 10, 1)
        [3, 6, 9]
    """
    res = []
    for i in range(start, end, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            res.append(i)
    return res

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Оценивает эмоциональную окраску текста.

    Подсчитывает баллы: +1 за каждое позитивное слово, -1 за негативное.
    Учитывает восклицательные знаки (умножает на 1.5) и вопросительные (умножает на 0.3).

    Args:
        text (str): анализируемый текст
        positive_words (list): список позитивных слов
        negative_words (list): список негативных слов

    Returns:
        float: оценка настроения (округлённая до 1 знака)

    Пример:
        >>> sentiment_score("I love Python!", ["love"], ["hate"])
        1.5
        >>> sentiment_score("I hate this!", ["love"], ["hate"])
        -1.5
    """

    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    count = 0
    
    for word in words:
        if word in positive_words:
            count+= 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            count -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            count *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            count *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(count, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def to_binary_string(number, counter=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    """
    Преобразует число в строку с его двоичным представлением.

    Логика функции содержит намеренный подвох
    При количестве итераций больше 10 строка разворачивается,
    что может давать неверный результат для больших чисел.

    Args:
        number (int): число для преобразования
        counter (int, optional): счётчик итераций. По умолчанию 0.

    Returns:
        str: двоичное представление числа (или "0", если число 0)

    Пример:
        >>> to_binary_string(10)
        '0101'
    """
    result = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если number = 0 падает, но заказчик сказал "и так сойдёт"
        result.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2  # магия. не трогать!!!
        counter += 1 # счётчик дней, недель, часов? хз, в ТЗ не было
    if counter > 10:  # 10 взял из головы, потом поменяю (нет)
        result.reverse() # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, result)) if result else "0"  # FIXME: работает — не трогай

print(to_binary_string(10))
