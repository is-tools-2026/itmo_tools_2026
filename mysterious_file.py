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
# print(make_tea(3200, 4))

# Функция 1

def bought_products(money, price_per_item, items_count):
    """
    Вычитает сумму за покупку одинаковых товаров из общей суммы денег у пользователя 

    Args:
        money (int): Число денег у пользоавтель
        price_per_item (float): Цена одного товара
        items_count (int): Число одинаковых товаров

    Returns:
        int / float: Оставшиеся деньги у пользователя
        str: В противном случае "Недостаточно денег"
    
    Example:
        >>> bought_products(100, 10, 5)
    50
        
        >>> bought_products(100, 100, 2)
    "Недостаточно денег"
    
    """
    
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(bought_products(100, 10, 5))
# print(bought_products(100, 100, 2)) 

# Функция 2

def is_in_list(day):
    
    """
    Делает проверку на наличие элемента в списке

    Args:
        day (str): Элемент, наличие которого мы хотим проверить
    
    Returns:
        bool: True - есть элемент, False - нет элемента
    Examples:
        >>> is_in_list("Суббота")
    True
        
        >>> is_in_list("С")
    False
    """
    
    # Надо подать прошение на включение Пятницы. 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_in_list("Суббота"))
# print(is_in_lidt("С"))

# Функция 3

def is_even(parametr):
    
    """
    Ф-ция, делающая проверку чётное ли число
    
    Args:
        parametr (int): Элемент, который мы хотим проверить
    Returns:
        bool: True - Кратно 2, False - не кратно 2
    Examples:
        >>> is_even(2)
    True
    
        >>> is_even(3)
    False
    """
    return parametr % 2 == 0

print(is_even(2))
# print(is_even(3))

# Функция 4

def multiples_of_3(prm1, prm2, step = 1):
    
    """ 
    Ф-ция возвращает список чисел, кратных 3
    
    Args:
        
        prm1(int) - Начало дипазона перебора индексов
        
        prm2(int) - Конец диапозона перебора индексов
        
        step(int) - Шаг перебора индексов
            - Если при вызове ф-ции шаг(step) не обозначаем => 
                step = 1
            - Если при вызове ф-ции шаг(step) обозначаем => 
                step = <введённое число>
        
    Returns:
    
            list: Список индексов списка чисел, делящихся на 3
        
    Examples:
    
    >>> 1) Input: 
        - multiples_of_3(0, 13)
       Output: 
        - [0, 3, 6, 9]
    
    >>> 2) Input: 
        - multiples_of_3(0, 13, 2)
       Output: 
        - [0, 6, 12]

    >>> 3) Input: 
        - multiples_of_3(0, 4, 1)
       Output: 
        - [0, 3]
    
    """
    
    res = []
    
    for i in range(prm1, prm2, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            res.append(i)
    return res

# tests
# num = int(input()) + 1
# step = int(input())
print(multiples_of_3(0, 4, 1))

# Функция 5

def sentiment_score(txt, pos, neg):
    """
    Функция возвращает коэфицент (оценку) того, на сколько сильно текст был эмоционально окрашен 

    Args:
        txt (str): Строка, которую будет оценивать функция
        pos (list): Массив положительных качеств (прилагательных)
        neg (list): Массив негативных качеств (прилагательных)

    Returns:
        float: Коэфицент эмоциональной окраски текста, округлённый до десятых 
    
    Examples:
    
    >>> sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]) 
    1.5
    
    >>> sentiment_score("love like enjoy", ["love", "like", "enjoy"], ["hate"]) 
    3.0

    >>> sentiment_score("Do I love! Python", ["love"], ["hate"])
    0.0
    """
    
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = txt.lower().split()
    ratio = 0
    
    for word in words:
        if word in pos:
            ratio += 1  # плюс балл за позитив, можно ещё два
        elif word in neg:
            ratio -= 1  # минус балл за негатив, грустно стало

        if word.endswith('!'): 
            ratio *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            ratio *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(ratio, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))
# tests
# print(sentiment_score("love like enjoy", ["love", "like", "enjoy"], ["hate"]))
# print(sentiment_score("Do I love! Python", ["love"], ["hate"]))

# Функция 6

def transform_into_binary(num, count = 0):  # TODO: переименовать, Витя опять не согласовал нейминг
    
    """
    Функция делает перевод числа из десятичной системы счистления в двоичную и выводит результат. В текущей версии переменная count не выводится 

    Args:
        num (int): Число в десятичной системы счистления
        count (int): Количество итераций
    
    Returns:
        str: Строка из символов входящего числа в двоичной системе счистления
    
    Examples:
        
        >>> transform_into_binary(10)
        '0101'
        
        >>> transform_into_binary(10, 3) 
        ('0101', 7)

        >>> transform_into_binary(12)
        ('1100', 4)
        
        >>> transform_into_binary(12, 23)
        ('1100', 27)
    """
    
    res = []  # тут будет результат, но я не уверен
    
    while num > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        res.append(num % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        num //= 2  # магия. не трогать!!!
        count += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
        
    if count > 10:  # 10 взял из головы, потом поменяю (нет)
        res.reverse()  # разворот, потому что иначе клиент жаловался
        
    return ''.join(map(str, res)) if res else "0"  # FIXME: работает — не трогай

print(transform_into_binary(10))
# tests
# print(transform_into_binary(10))
# print(transform_into_binary(10, 3))
# print(transform_into_binary(12))
# print(transform_into_binary(12, 23))
