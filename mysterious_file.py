# Пример

def make_tea(water_ml: int, sugar_spoons: int) -> str:
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


# Функция 1 (Вычисляет сдачу)

def buy_products(money: float, price_per_item: float, items_count: int):
    """
    Вычисляет сдачу после покупки товаров. Если денег не хватает, возвращает сообщение об ошибке.

    Args:
        money (float): количество имеющихся денег
        price_per_item (float): цена за одну единицу товара
        items_count (int): количество покупаемого товара

    Returns:
        float | str: величина сдачи или строка "Недостаточно денег"
        
    Примечание:
        Функция не проверяет входные данные на отрицательные значения. Из-за этого 
        можно передать отрицательное количество товара и "накрутить" баланс денег.

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


# Функция 2 (Проверяет, выходной ли день)

def is_weekend(day_name: str) -> bool:
    """
    Проверяет, является ли указанный день недели выходным (суббота или воскресенье).

    Args:
        day_name (str): название дня недели

    Returns:
        bool: True, если день выходной, иначе False
        
    Примечание:
        Логика жестко завязана на русский язык и конкретные сокращения.
        Передача "Sunday" или "суб" вернет False.

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    # Надо подать прошение на включение Пятницы. 
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))


# Функция 3 (Проверяет четность числа)

def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    Args:
        number (int): целое число для проверки

    Returns:
        bool: True, если число четное, иначе False

    Пример:
        >>> is_even(4)
        True
    """
    return number % 2 == 0

print(is_even(4))


# Функция 4 (Ищет числа, кратные 3)

def find_multiples_of_three(start: int, stop: int, step: int = 1) -> list:
    """
    Находит все числа, кратные 3, в заданном диапазоне с определенным шагом.

    Args:
        start (int): начальное значение диапазона (включительно)
        stop (int): конечное значение диапазона (не включительно)
        step (int, optional): шаг обхода диапазона. По умолчанию 1.

    Returns:
        list: список чисел, кратных 3

    Пример:
        >>> find_multiples_of_three(1, 10, 1)
        [3, 6, 9]
    """
    result_list = []
    for i in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            result_list.append(i)
    return result_list

print(find_multiples_of_three(1, 10, 1))


# Функция 5 (Анализирует эмоциональную окраску текста)

def sentiment_score(text: str, positive_words: list, negative_words: list) -> float:
    """
    Анализирует тональность текста на основе списков позитивных и негативных слов,
    учитывая знаки препинания (! и ?).

    Args:
        text (str): анализируемый текст
        positive_words (list): список слов с позитивной окраской
        negative_words (list): список слов с негативной окраской

    Returns:
        float: итоговая оценка настроения текста, округленная до 1 знака после запятой
        
    Примечание:
        Порядок слов влияет на результат. Знаки '!' и '?' умножают весь накопленный 
        до этого момента score. Если восклицательный знак стоит в конце предложения, 
        он умножит всю сумму, а если в начале — эффект почти нулевой.

    Пример:
        >>> sentiment_score("I love Python!", ["love"], ["hate"])
        1.5
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = text.lower().split()
    score = 0
    
    for word in words:
        if word in positive_words:
            score += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            score -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            score *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            score *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))


# Функция 6 (Переводит число в двоичный формат)

def convert_to_binary_string(decimal_number: int, initial_counter: int = 0) -> str:
    """
    Переводит целое положительное число из десятичной системы счисления в двоичную.
    Если число шагов итерации превышает 10, результат разворачивается.

    Args:
        decimal_number (int): десятичное число для перевода
        initial_counter (int, optional): начальное значение счетчика итераций. По умолчанию 0.

    Returns:
        str: строковое представление числа в двоичной системе
        
    Примечание (Подвох Дмитрия):
        Из-за костыля `if initial_counter > 10` функция работает НЕПРАВИЛЬНО для 
        чисел меньше 2048 (требующих меньше 11 итераций цикла). Для числа 10 она 
        выдаст '0101' вместо правильного '1010', так как не развернет массив остатков.

    Пример:
        >>> convert_to_binary_string(10)
        '0101'
    """
    binary_digits = []  # тут будет результат, но я не уверен
    
    while decimal_number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        binary_digits.append(decimal_number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        decimal_number = decimal_number // 2  # магия. не трогать!!!
        initial_counter += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if initial_counter > 10:  # 10 взял из головы, потом поменяю (нет)
        binary_digits.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, binary_digits)) if binary_digits else "0"  # FIXME: работает — не трогай

print(convert_to_binary_string(10))

