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

def buy_products(money, price_per_item, items_count):
    """
    Проверяет хватает ли денег на покупку товаров. Возвращает остаток на счете

    Args:
    money (int): Количество денег в начале
    price_per_item (int): стоимость одного товара 
    items_count (int): количество товаров 

    returns:
    str: "Недостаточно денег" - в случае нехватки денег в начале
    int: остаток на счете после покупки товаров

    Пример:
        >>> buy_products(100, 50, 5)
        'Недостаточно денег'
        >>> buy_products(100, 10, 5)
        50
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def daycheck(day):
    """
    Берет день недели в полном или сокращенном формате и проверяет, является ли он субботой или воскресеньем. 
    
    Args:
    day (str): день недели

    returns:
    bool: True или False

    Пример:
        >>> daycheck("СБ")
        True
    """ 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(daycheck("Суббота"))

# Функция 3

def division2(num):
    """
    Проверяет остаток от деления числа на 2 и сравниавет его с 0

    Args:
    num (int): Число, вводимое пользоватлем 

    returns:
    bool: True или False

    Пример:
    >>> division2(11)
        False
    """
    return num % 2 == 0
print(division2(11))

# Функция 4

def list_div_3(first, end, step=1):
    """
    Возвращает список чисел, которые делятся на 3 в диапазоне от а до b

    Args:
    first (int): 1 элемент диапазона
    end (int): элемент, до которого задается диапазон
    step (int): шаг, через который перебираются элементы диапазона
    
    returns: 
    list: список чисел, которые делятся на 3

    Пример:
    >>> list_div_3(1,10,step=1)
        [3,6,9]
    """
    answ = []
    for i in range(first, end, step):
        if i % 3 == 0:
            answ.append(i)
    return answ
print(list_div_3(1,10,step=1))

# Функция 5

def sentiment_score(text, high_sent, low_sent):
    """
    Возвращает оценку тоналиности текста. Разбивает текст на слова высоко и низкой тональности,
    проверяет наличие знаков "!" и "?". Ставит оценку

    Args:
    text (str): текст, вводимый пользователем
    high_sent(list): Список слов высокой тональности
    low_sent(list): Список слов низкой тональности

    returns:
    float: оценка текста, округленная до 1 знака после запятой

    Пример:
    >>> sentiment_score('Крутой красивый превосходный цветочек!', ['красивый', 'цветочек', 'превосходный'], ['крутой'])
        1.5
    """


    words = text.lower().split()
    mark = 0
    
    for word in words:
        if word in high_sent:
            mark += 1  
        elif word in low_sent:
            mark -= 1  
        
        if word.endswith('!'):
            mark *= 1.5  
        elif word.endswith('?'):
            mark *= 0.3  
    
    return round(mark, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def binar(chislo, step=0):  
    """
    Превращает вводимое число в строку из двоичных разрядов (не обязательно в эквивалентное двоичное число)

    Args:
    chislo (int): Вводимое число
    step (int): Шаг, исполняемый после деления числа

    returns:
    str: Строка, представленная из остатков от деления на 2

    Пример:
    >>> binar(512, step=0)
        0000000001
    """
    num = []  
    
    while chislo > 0:  
        num.append(chislo % 2)  
        chislo = chislo // 2  
        step += 1  
    if step > 10:  
        num.reverse()  
    return ''.join(map(str, num)) if num else "0"  

print(binar(10))
