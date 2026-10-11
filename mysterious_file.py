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
    Считает сдачу. 

    Args:
        money (int): колво денег покупателя
        price_per_item (int): цена за товар
        items_count (int): колво закупаемого товара
     
    Returns:
        int/str: возвращает сдачу либо "Недостаточно денег"

    Example:
        buy_products(100, 10, 5) вернет 50
        buy_products(10, 10, 5) вернет "Недостаточно денег"
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check_weekend_or_not(day):
    """
    Функция проверяет, указанный день недели выходной или нет.
    
    Args:
        day (str): день недели
    
    Returns:
        bool: True, если день выходной, False, если нет

    Example:
        check_weekend_or_not("пт") вернет False
        check_weekend_or_not("вс") вернет True
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check_weekend_or_not("Суббота"))

# Функция 3

def is_number_even(number):
    """
    Функция проверяет, четное число или нет
    
    Args:
        number (int): проверяемое число
    
    Returns:
        bool: True, если четное, False, если нет
    
    Example:
        is_number_even(1) вернет Flase
        is_number_even(2) вернет True
    """
    return number % 2 == 0

# Функция 4

def find_numbers_multiple_of_three(firstnumber, lastnumber, step=1):
    """
    Функция ищет числа кратные трем среди чисел от firstnumber до lastnumber
    
    Args:
        firstnumber (int): первое число диапазона
        lastnumber (int): последнее число диапазона не включительно
        step (int): шаг цикла, равен 1 по умолчанию
    
    Returns:
        ist[int], в массиве числа, кратные трем из диапазона
    
    Example:
        find_numbers_multiple_of_three(1, 7, 1) вернет [3, 6]
    """
    arr = []
    for i in range(firstnumber, lastnumber, step):
        if i % 3 == 0:
            arr.append(i)
    return arr

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Функция вычисляет позитивность текста(text) по правилам: если в тексте есть слова из 
    списка позитивных слов positive_words, к счету(score) прибавляется балл, если есть 
    слово из негативных слов negative_words, балл отнимается. Если в тексте есть
    вопросительный или восклицательный знак, счет умножается соответственно либо на 0.3,
    либо на 1.5. Счет округлен до 1 знака после запятой.
    
    Args:
        text (str): проверяемый текст
        positive_words (list[str]): позитивные слова
        negative_words (list[str]): негативные слова
    
    Returns:
        float: итоговый счет
    
    Example:
        print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))
        вернет 1.5
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


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def binary_digit(number, steps=0):  
    """
    Функция возвращает перевернутую двоичную запись поданного числа в виде строки, но если счетчик steps
    больше 10, то запись переворачивается (например, не 010111, а 111010)
    
    Args:
        number (int): преобразуемое число
        steps (int): счетчик, по умолчанию 0
    
    Returns:
        list[str]: строка с перевернутой двоичной записью числа, переворачивается, если 
        счетчик > 10. Если число равно нулю, то возвращается 0 (т.к. тогда массив arr = 0)
    
    Example:
        print(binary_digit(10)) возвращает "0101"
    """
    arr = [] 
    
    while number > 0:  
        arr.append(number % 2)  
        number = number // 2  
        steps += 1  
    if steps > 10: 
        arr.reverse()  
    return ''.join(map(str, arr)) if arr else "0"  

print(binary_digit(10))
