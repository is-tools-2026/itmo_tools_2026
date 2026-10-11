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
    Функция сравнивает баланс со стоимостью покупки и возвращает сдачу. 
    Если баланса не хватает выводит сообщение о нехватке средств

    Args:
        money (int): Баланс на счету
        price_per_item (int): Стоимость одного предмета
        items_count (int): Количество предметов

    Returns:
        str: Сообщение о нехватке средств
        int: Сдачу после покупки

    Пример:
        >>> buy_products(200,50,5)
            'Недостаточно денег'
        >>> buy_products(777,2,111)
            555
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def daycheck(day):
    """
    Проверяет,выходной ли сегодня день

    Args:
        day (str): день недели

    Returns:
        bool: результат проверки заданного с заранее записанным

    Пример:
        >>> daycheck("Понедельник")
        false
        >>> daycheck("сб")
        true
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(daycheck("Суббота"))

# Функция 3

def evencheck(x):
    """
    Проверяет,чётное число или же нет

    Args:
        x (int): число для проверки

    Returns:
        bool: результат проверки чётности

    Пример:
        >>> evencheck(111111)
        false
        >>> evencheck(100010001111000101000110001000010)
        true
    """
    return x % 2 == 0

# Функция 4

def checktrio(a, b, c=1):
    """
    Проверяет последовательность чисел на делимость на три

    Args:
        a (int): начало последовательности
        b (int): конец последовательность
        c (int): шаг последовательности

    Returns:
        list: список выявленных чисел

    Пример:
        >>> checktrio(1, 12, c=1)
        [3,6,9]
    """
    result = []
    for i in range(a, b, c):
        if i % 3 == 0:
            result.append(i)
    return result

# Функция 5

def sentiment_score(text, good_wd, bad_wd):
    """
    Алгоритм,который понимает эмоции, вложенные в текст

    Args:
        text (str): заданный текст
        good_wd (list): список хороших слов
        bad_wd (list): список негативных слов

    Returns:
        float: коэффицент эмоциональности текста

    Пример:
        >>> sentiment_score("Всем привет! Я очень хороший и добрый человек. Наверное?", ["добрый","хороший","весёлый"], ["злой","плохой"])
        0.6
    """
    words = text.lower().split()
    score = 0
    
    for word in words:
        if word in good_wd:
            score += 1 
        elif word in bad_wd:
            score -= 1
        
        if word.endswith('!'):
            score *= 1.5
        elif word.endswith('?'):
            score *= 0.3
    
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def binary(x, y=0):
    """
    Функция,что переводит число в двоичную систему счиселния

    Args:
        x (int): число для перевода
        y (int): счётчик

    Returns:
        str: число в двоичной системе счисления

    Пример:
        >>> binary(123)
        '1111011'
    """
    z = []
    
    while x > 0:
        z.append(x % 2)
        x = x // 2
        y += 1
    if y > 10:
        z.reverse()
    return ''.join(map(str, z)) if z else "0"

print(binary(10))
