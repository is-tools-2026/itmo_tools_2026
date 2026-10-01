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

def calculate_change(money, price_per_item, items_count):
    """
    Вычисляет сдачу при покупке товаров.

    Args:
        money (int/float): сумма имеющихся денег
        price_per_item (int/float): цена одного товара
        items_count (int): количество приобретаемых товаров

    Returns:
        int/float/str: оставшаяся сдача или сообщение о нехватке средств

    Пример:
        >>> calculate_change(100, 10, 5)
        50
    """

    total = price_per_item * items_count

    if total > money:
        return "Недостаточно денег"

    return money - total

print(calculate_change(100, 10, 5))

# Функция 2

def is_weekend(day):
    """
    Проверяет, является ли день недели выходным.

    Args:
        day (str): название дня недели или его краткое обозначение
    
    Returns:
        bool: True, если день выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """

    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number):
    """
    Проверяет, является ли число четным.

    Args:
        number (int): проверяемое число
    
    Returns:
        bool: True, если число четное, иначе False

    Пример:
        >>> is_even(4)
        True
    """

    return number % 2 == 0

print(is_even(4))

# Функция 4

def get_multiples_of_three(start, stop, step=1):
    """
    Формирует список чисел кратных 3 из заданного диапазона.

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включительно)
        step (int/optional): шаг итерации, по умолчанию 1
    
    Returns:
        list[int]: список чисел, делищихся на 3 без остатка

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
    """

    result = []

    for num in range(start, stop, step):

        if num % 3 == 0:
            result.append(num)

    return result

print(get_multiples_of_three(1, 10))

# Функция 5

def analyze_sentiment(text, positive_words, negative_words):
    """
    Оценивает эмоциональную окраску текста на основе списка ключевых слов.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных слов
        negative_words (list[str]): список негативных слов
    
    Returns:
        float: итоговая оценка настроения текста

    Пример:
        >>> analyze_sentiment("I love Python!", ["love", "like"], ["hate"])
        1.5
    """

    words = text.lower().split()
    score = 0
    
    for word in words:
        if word in positive_words:
            score += 1  # плюс балл за позитив
        elif word in negative_words:
            score -= 1  # минус балл за негатив
        
        if word.endswith('!'):
            score *= 1.5  
        elif word.endswith('?'):
            score *= 0.3  
    
    return round(score, 1)


print(analyze_sentiment("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def to_binary_string(number, counter=0): 
    """
    Переводит целое неотрицательное число в строку двоичного представления.

    Args:
        number (int): число для перевода в двоичную систему
        counter (int/optional): начальный счетчик итераций, по умолчанию 0
    
    Returns:
        str: двоичное представление числа в виде строки

    Пример:
        >>> to_binary_string(10)
        '1010'
    """

    bits = []  
    
    while number > 0:  
        bits.append(number % 2) 
        number = number // 2  
        counter += 1 

    if counter > 10: 
        bits.reverse()  

    return ''.join(map(str, bits)) if bits else "0" 

print(to_binary_string(10))
