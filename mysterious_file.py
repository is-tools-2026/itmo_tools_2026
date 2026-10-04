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
    Считает сдачу после покупки одинаковых товаров.

    Args:
        money (int, float): сколько денег у покупателя
        price_per_item (int, float): цена одного товара
        items_count (int): количество товаров

    Returns:
        int | float | str: сдача, а если денег не хватает, то строка
            "Недостаточно денег"

    Пример:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(100, 30, 5)
        'Недостаточно денег'
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total_price = price_per_item * items_count
    if total_price > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total_price

print(calculate_change(100, 10, 5))

# Функция 2

def check(d):
    # Надо подать прошение на включение Пятницы. 
    return d.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check("Суббота"))

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
