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

def change(money, price_per_item, items_count):
    """
    Вычисление сдачи после покупки заданного количества товаров 
    Args:
        money(int): сумма денег 
        price_per_item(int):цена за один товар 
        items_count(int): количесво товаров 

    Returns:
        int: сдача после покупки
        str: "Недостаточно денег" , если изначальная сумма денег меньше total
    Пример:
        >>>  change(500, 10, 2)
        480
        >>> change(100, 100, 2)
        'Недостаточно денег'
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(change(100, 10, 5))

# Функция 2

def is_a_day_off(day):
    """
    Проверяет является ли запрошеный день выходным 
    Args:
        day(str):название дня недели (без учета регистра)
    Returns:
        bool: True, если "сб", "вс", "суббота", "воскресенье"
            False во всех других слуиях 
    Пример:
        >>> is_a_day_off("Суббота")
        True
        >>> is_a_day_off("Пн")
        False
    """
    # Надо подать прошение на включение Пятницы. 
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_a_day_off("Суббота"))

# Функция 3

def even_number(number):
    """
    Проверяет является ли число четным 
    Args:
        number(int): число для проверки
    Returns:
        bool: True - четное
            False - нечетное 
    Пример:
        >>> even_number(2)
        True
        >>> even_number(77)
        False
    """
    return number % 2 == 0

# Функция 4

def numbers_multiples_of_three(start,stop, step=1):
    """
    Проверяет явлиется ли числ кратным трем, если да, то добавляет в списак 
    Args:
        start(int): начальное число входа в цикл 
        stop(int): конечная граница 
        step(int): шаг в цикле
    Returns:
        list[int]: список чисел, кратных трем 
    Пример:
        >>> numbers_multiples_of_three(1, 10 , 1)
        [3,6,9]
    """
    list_of_numbers = []
    for number in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if number % 3 == 0:
            list_of_numbers.append(number)
    return list_of_numbers

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Функция вычисляет настроение через слова и знаки препинания 
    Args:
        text(str): текст для анализа
        positive_words(list[str]): список позитивных слов
        negative_words(list[str]): списое негативных слов
    Returns:
        int или float: оценка настроения 
    Пример:
        >>> sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"] )
        1.5
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    score = 0
    
    for word in words:
        if word in  positive_words:
            score += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            score -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            score *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def converting_a_number_to_binary(number, score=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    """
    Переводит числа в двоичную систему и в зависимости от количества итераций переворачивает или выводит в прямом порядке
    Args:
        number(int): число для перевода
        score(int): счетчик итераций 
    Returns:
        str:двоичные цифры в обратном порядке , если  счетчик меньше или равнен 10 , иначе в пярмом порядке , для чисел меньших или равных 0 возращает "0"
    Пример:
        >>> converting_a_number_to_binary(10)
        '0101'
    """
    binary_list = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        binary_list.append(number% 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number  // 2  # магия. не трогать!!!
        score+= 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if score > 10:  # 10 взял из головы, потом поменяю (нет)
        binary_list.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, binary_list)) if binary_list else "0"  # FIXME: работает — не трогай

print(converting_a_number_to_binary(10))
