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

def buy_products(money: float, price_per_item: float, items_count: int) -> float | str:
    """
    Вычисляет сдачу после покупки товаров по одинаковой цене.

    Args:
        money (float): деньги покупателя;
        price_per_item (float): цена товара;
        items_count (int): количество покупаемого товара.

    Returns:
        float: размер сдачи, если денег покупателя достаточно для покупки;
        str: строка "Недостаточно денег", если денег покупателя не достаточно для покупки.

    Пример:
        >>> buy_products(510, 150, 3)
        60
        >>> buy_products(510, 150, 4)
        "Недостаточно денег"
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check_weekend(day: str) -> bool:
    """
    Проверяет, является ли указанный день недели выходным.

    Args:
        day (str): название дня недели.

    Returns:
        bool: True, если данный день недели является субботой или воскресеньем, иначе - False.

    Пример:
        >>> check_weekend("вс")
        True
        >>> check_weekend("пятница")
        False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check_weekend("суббота"))

# Функция 3

def is_even_number(number: int) -> bool:
    """
    Проверяет, является ли указанное число чётным.

    Args:
        number (int): целое число

    Returns:
        bool: True, если данное число чётное, иначе - False.

    Пример:
    >>> is_even_number(156)
    True
    >>> is_even_number(77)
    False
    """
    return number % 2 == 0

# Функция 4

def add_multiplicity_3(start: int, finish: int, step: int = 1) -> list[int]:
    """
    Добавляет в список только те элементы из данного диапазона, которые кратны 3.

    Args: 
        start (int): число - начало диапазона;
        finish (int): число - конец диапазона;
        step (int): по умолчанию 1 - шаг перебора.

    Returns:
        list[int]: список чисел, кратных 3.

    Пример:
    >>> add_multiplicity_3(18, 52, 1)
    [18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
    """
    numbers = []
    for i in range(start, finish, step):
        if i % 3 == 0:
            numbers.append(i)
    return numbers

# Функция 5

def sentiment_score(text: str, positive_words: list[str], negative_words: list[str]) -> float:
    """
    Определяет тональность текста, исходя из списков позитивных и негативных слов.

    Args: 
        text (str): исходный текст;
        positive_words (list[str]): список позитивных слов;
        negative_words (list[str]): список негативных слов;

    Returns:
        result (float): оценка тональности текста, округленная до 1 знака после запятой.

    Пример:
        >>> sentiment_score("Какой хороший день!", ["хороший", "отличный", "замечательный"], ["плохой", "отвратительный", "грустный"])
        1.5
        >>> sentiment_score("Снова отвратный день, да?", ["хороший", "отличный", "замечательный"], ["плохой", "отвратительный", "грустный", "отвратный"])
        -0.3
    """
    words = text.lower().split()
    result = 0
    
    for word in words:
        if word in positive_words:
            result += 1  
        elif word in negative_words:
            result -= 1 
        
        if word.endswith('!'):
            result *= 1.5  
        elif word.endswith('?'):
            result *= 0.3 
    
    return round(result, 1)

print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def to_binary_numb_system(number: int, iteration: int=0) -> str:
    """
    Переводит целое неотрицательное число в двоичную систему счисления.
    Важно! Список остатков разворачивается, только если количество итераций превысило 10. Это приводит к тому, что
    для чисел меньше 1024 двоичная запись возвращается в перевёрнутом виде.
    То есть:
    Для 1024: iteration = 11, условие 11 > 10 истина → разворот есть → результат 10000000000 (правильно).
    Для 10: iteration = 4, условие 4 > 10 ложь → разворота нет → результат 0101 (неправильно).
    
    Args:
        number (int): неотрицательное число;
        iteration (int): по умолчанию 0 - счётчик итераций;

    Returns:
        str: двоичное представление числа

    Пример:
        >>> to_binary_numb_system(1024)
        '10000000000'
        >>> to_binary_numb_system(10)
        '0101'
    """ 
    remainders = [] 
    
    while number > 0:
        remainders.append(number % 2)  
        number = number // 2  
        iteration += 1  
    if iteration > 10:  
        remainders.reverse() 
    return ''.join(map(str, remainders)) if remainders else "0"  

print(to_binary_numb_system(10))
