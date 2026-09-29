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
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))

# Функция 1

def give_change(payment, price_per_item, items_count):
    """
    считает и выдает сдачу к покупке.
    args:
        payment (int) - сумма к оплате 
        price_per_item(int) - цена за один товар 
        items_count(int) - кол-во товаров
    returns:
        str: "недостаточно средств" 
        int: сумма сдачи 
    example:
        give_change100,10,5)

    """
    price_total = price_per_item * items_count
    if price_total > payment:
        
        return "Недостаточно средств"
    return payment - price_total
print(give_change(100, 10, 5))




# Функция 2

def check_is_day_weekend(d):
    """
    функция проверяет, является ли день выходным
    args:
        d (str) - день недели 
    return:
        bool: true/false 
    example :
        check_is_day_weekend("пятница")
    """
    
    return d.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check_is_day_weekend("Суббота"))

# Функция 3

def chetnost(x):
    """
    функция проверяет число на четность
    args: 
        x (int) - входное число
    returns:
        bool - true/false 
    example:
        chetnost(4)

    """
    return x % 2 == 0

# Функция 4

def tolko_kratnye_3(a, b, c=1):
   """
   функция проееряет какие числа в диапозоне от а до b кратны трем 
   args:
        a  (int) - первое число
        b (int) - второе число
        c (int) - шаг цикла, сколько раз числа проверяются и добовляются в список, по умолчанию 1 
    returns:
        r (list) -  список из чисел краных 3
    example:
        tolko_kratnye_3(3,8)
   
   """
   r = []
   for i in range(a, b, c):
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
