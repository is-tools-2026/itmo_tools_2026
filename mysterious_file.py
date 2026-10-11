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
    Вычисляет сдачу после покупки определенного количества товаров

    Args:
        money (int or float): количество денег у покупателя
        price_per_item (int or float): цена за одну единицу товара
        items_count (int or float): количество приобретаемых единиц \
            товара или вес(для товаров наразновес)

    Returns:
        int or float or str: сдача или строка "Недостаточно денег", \
            если общая стоимость превышает бюджет

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

def is_weekend(d):
    """
    Проверяе, введенный день выходной или нет

    Args:
        day_name (str): название дня недели (в короткой или полной форме)

    Returns:
        bool: True, если день выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    # Надо подать прошение на включение Пятницы. 
    return d.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number):
    '''
    Проверяет четность числа

    Args:
        number (int): число, четность коорого проверяется

    Returns:
        bool: 1, если четное, 0, если нечетное

    Пример:
        >>> is_even(67)
        0
    '''
    return number % 2 == 0

print(is_even(67))

# Функция 4

def are_divisible_by_3_in_range (start, end, step=1):
    """
    находит все числа, кратные 3-м в заданном диапозоне с шагом(по умолчанию 1)

    Args:
        start (int): начальное значение диапазона (включая)
        end (int): конечное значение диапазона (не включая)
        step (int)(optional): шаг проверки. По умолчанию равен 1 

    Returns:
        list: список целых чисел, которые делятся на 3 без остатка

    Пример:
        >>> are_divisible_by_3_in_range(0, 9)
        [0, 3, 6]
    """
    divisible_by_3_nums = []
    for i in range(start, end, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            divisible_by_3_nums.append(i)
    return divisible_by_3_nums

print(are_divisible_by_3_in_range(0, 9))

# Функция 5

def sentiment_score(text, list_of_positive_words, list_of_negative_words):
    """
    вычисляет насколько текст был радостным/грустным, сверяясь с позивным и негативным \
        списком слов и учитывая знаки препинания (? или !)

    Args:
        text (str): текст, который надо оценить
        list_of_positive_words (list[str]): список слов, которые считаются позитивными
        list_of_negative_words (list[str]): список слов, которые считаются \
            негативными(может пересекаться с позитивным списком, но тогда это слово не влияет)

    Returns:
        int: оценка позитивности текста (округленная до десятых)

    Пример:
        >>> sentiment_score("Хочу пельмени!", ["пельмени", "пицца", "котлетки", "пюрешка"], ["сюрстрёминг", "голод"])
        1,5
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    list_of_words = text.lower().split()
    score = 0
    
    for word in list_of_words:
        if word in list_of_positive_words:
            score += 1  # плюс балл за позитив, можно ещё два
        elif word in list_of_negative_words:
            score -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            score *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(score, 1)
print(sentiment_score("Хочу пельмени!", ["пельмени", "пицца", "котлетки", "пюрешка"], ["сюрстрёминг", "голод"]))
#print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def convert_to_binary_str(dec_number, defoult_counter=0):
    '''
    Переводит десятичную запись числа в двоичную. Запись перевернута, если число\
        меньше 2 в степене (10 - (второй аргумент))
    
        Args:
            dec_number (int): число для перевода в двоичную систему
            defoult_counter (int)(optional): аргумент, определяющий, до какого числа запись будет перевернутой
        
        Returns:
            str: запись числа в bin системе
        
        Пример:
            >>> convert_to_binary_str(2**5-2, 5)
            "01111"
    '''
    list_of_bin_digits = []
    
    while dec_number > 0:
        list_of_bin_digits.append(dec_number % 2)
        dec_number //= 2
        defoult_counter += 1
    if defoult_counter > 10:
        list_of_bin_digits.reverse()
    return ''.join(map(str, list_of_bin_digits)) if list_of_bin_digits else "0"

print(convert_to_binary_str(2**5-2, 5))
