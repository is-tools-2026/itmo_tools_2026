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

def sentiment_score(t, p_w, n_w):
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = t.lower().split()
    s = 0
    
    for word in words:
        if word in p_w:
            s += 1  # плюс балл за позитив, можно ещё два
        elif word in n_w:
            s -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            s *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            s *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(s, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def f(x, y=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    z = []  # тут будет результат, но я не уверен
    
    while x > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        z.append(x % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        x = x // 2  # магия. не трогать!!!
        y += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if y > 10:  # 10 взял из головы, потом поменяю (нет)
        z.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, z)) if z else "0"  # FIXME: работает — не трогай

print(f(10))
