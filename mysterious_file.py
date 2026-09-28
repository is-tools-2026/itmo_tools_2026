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
    Считает итоговую сумму за покупку товаров и остаток после покупки

    Args:
        money(int): кол-во имеющихся денег денег
        price_per_item(int): цена за единицу товара
        items_count(int): кол-во товаров

    Returns:
        str: если не хватает денег на покупку "Недостаточно денег"
        int: если денег хватает, считает сколько останется после покупки

    Пример:
        buy_products(100, 10, 5) #50

    """
    total = price_per_item * items_count

    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check(day): 
    """
    Проверяет находится ли переданное в прогармму слово(аббривеатура слова) в списке

     Args:
        day(str): слово или аббривеатура дня недели

    Returns: 
        bool: значение,которое отвечает на вопрос:принадлежит ли слово списку?

    Пример: 
        print(check("понедельник")) #False
        print(check("воскресенье")) #True

    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check("понедельник"))

# Функция 3

def check_even(num):
    """
    Проверяет,является ли число чётным

    Args:
        num(int): число, которое необходимо проверить

    Returns:
        bool: значение,которое отвечает на вопрос:является ли число четным?

    Пример:
        print(check_even(4))  #True
        print(check_even(7))  #False

    """
    return num % 2 == 0

# Функция 4

def div3_in_range(start, end, step=1):
    """
    Возвращает числа,которые делятся на 3 без остатка, в заданном диапазоне

    Args:
        start(int): начало диапазона
        end(int): конец диапазона(не включается)
        step(int): шаг с которым идем по диапазону(установлен по умолчанию)

    Returns:
        list: список чисел кратных 3
    
    Пример:
        print(div3_in_range(2,15)) #[3, 6, 9, 12]

    """
    lst3 = []
    for i in range(start, end, step):
        if i % 3 == 0:
            lst3.append(i)
    return lst3

# Функция 5

def emotional_scale(text, positive, negative):
    """
    Вычисляет эмоциональную оценку текста на основе положительных и отрицательных слов
    
    Args: 
        text(str): текст тональность которого необходимо определить
        positive(list): список положительных слов
        negative(list): список отрицательных слов

    Returns:
        float: оценка эмоциональности текста,округлённая до десятых

    Пример:
        print(sentiment_score( "I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"] )) #1.5
        
    """
    words = text.lower().split()
    scale = 0
    
    for word in words:
        if word in positive:
            scale += 1  
        elif word in negative:
            scale -= 1  
        
        if word.endswith('!'):
            scale *= 1.5  
        elif word.endswith('?'):
            scale *= 0.3  
    
    return round(scale, 1)


print(emotional_scale("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def translation_into_binary(num, count=0):
    """ 
    Переводит число в двоичную систему счисления
    Если количество итераций больше 10, для корректного результата переворачивает полученный список цифр

    Args: 
        num (int): число которое необходимо перевести
        count (int): счётчик количества итераций(установлен по умолчанию)
        
    Returns: 
        str: строка с числом в двоичной системе
        
    Пример: 
        print(f(10)) #0101

    """
    binary = []  
    
    while num > 0:
        binary.append(num % 2) 
        num = num // 2
        count += 1  
    if count > 10:
        binary.reverse() 
    return ''.join(map(str, binary)) if binary else "0"

print(translation_into_binary(10))
