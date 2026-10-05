# Пример
"""
Набор небольших утилит, оставленных прошлым разработчиком.

Модуль содержит функции для подсчета сдачи, проверки выходных,
проверки четности, поиск чисел (кратных трем), оценки тональности текста и
перевода числа в двоичную строку.

Проверка примеров из документации:
    python -m doctest -v mysterious_file.py
"""


def make_tea(water_ml: int, sugar_spoons: int) -> str:
    """
    Готовит чай, смешивая воду и сахар.

    Args:
        water_ml (int): Объём воды в миллилитрах.
        sugar_spoons (int): Количество ложек сахара.

    Returns:
        str: Описание получившегося напитка.

    Пример:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))

# Функция 1

def calculate_change(money: int | float, price_per_item: int | float, items_count: int) -> int | float | str:
    """
    Вычисляет сдачу при покупке определенного количества товаров.

    Args:
        money (int | float): Сумма денег у клиента.
        price_per_item (int | float): Цена одного товара.
        items_count (int): Количество приобретаемых товаров.

    Returns:
        int | float | str: Сумма сдачи или сообщение о недостатке средств.
    
    Example:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(30, 10, 5)
        'Недостаточно денег'
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(calculate_change(100, 10, 5))

# Функция 2

def is_weekend(day_name: str) -> bool:
    """
    Проверяет, является ли указанный день недели выходным (суббота или воскресенье).

    Args:
        day_name (str): Название дня недели или краткое обозначение.
    Returns:
        bool: True, если день - выходной, иначе False.
    
        Example:
            >>> is_weekend("Суббота")
            True
            >>> is_weekend("вт")
            False
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def h(x):
    return x % 2 == 0

# Функция 4

def z(a, b, c=1):
    r = []
    for i in range(a, b, c):
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
