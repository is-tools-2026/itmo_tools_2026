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
    Считает сдачу с купленных товаров вычитая цену умноженную 
    на количество товаров из количества денег на руках.

    Args:
        money (int): сколько есть денег на руках
        price_per_item (int): цена товара 
        items_count (int): сколько штук будет покупатель брать
    
    Пример:
        >>>buy_products(100, 10, 5)
        '50'
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def check_if_weekend(weekend):
    """
    Проверяет введенный день недели на соответствие с выходным, функция lower делает из всех заглавных букв прописные.

    Args:
        weekend (str): день недели
    
    Пример:
        >>>check("Суббота")
        'True'
    """
    # Надо подать прошение на включение Пятницы. 
    return weekend.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check_if_weekend("Суббота"))

# Функция 3

def even(number_even):
    """
    Делает проверку числа на четность.

    Args:
        number_even (int): число
    
    Пример: 
        >>>even(100)
        'True'
    """
    return number_even % 2 == 0

print(even(100))

# Функция 4

def check_division_by_3(first_point, second_point, with_step=1):
    """
    Проверяет в промежутке от first_point до second_point, с шагом в with_step(если ничего не ввести, то шаг будет равен единице)
    какие из чисел делятся на 3, вводит нужные числа в список.

    Args:
        first_point (int): первая точка промежутка
        second_point (int): вторая точка промежутка
        with_step (int): с каким шагом будет идти фунция по промежутку
        checked_numbers_div_by_3 (list): числа которые делятся на 3
        numba (int): временная переменная, которая принимает очередное число из диапазона для проверки

    Пример:
        >>>check_division_by_3(9, 15, 2)
        '[9]'
    """
    checked_numbers_div_by_3 = []
    for numba in range(first_point, second_point, with_step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if numba % 3 == 0:
            checked_numbers_div_by_3.append(numba)
    return checked_numbers_div_by_3

print(check_division_by_3(9, 12, 2))

# Функция 5

def sentiment_score(phrase, positive_words, negative_words):
    """
    Смотрим с каким настроением написана фраза.

    Args:
        phrase (str): фраза которую мы провереяем
        positive_words (list): слова с позитивным настроением
        negative_words(list): слова с негативным настроением
        mood (int): считает с каким настроением был написан текст
        words (list): времменный список по которому мы проходим циклом for, список состоит из слов во фразе
        word (str): временная переменная которой мы проходимся по списку

    Пример:
        >>>print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))
        '1.5'
    """
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = phrase.lower().split()
    mood = 0
    
    for word in words:
        if word in positive_words:
            mood += 1  # плюс балл за позитив, можно ещё два
        elif word in negative_words:
            mood -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            mood *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            mood *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(mood, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def convert_to_binary_if(number_bit_count, bit_count=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    """
    Переводит число в двоичную систему исчесления
    Возвращает в обратном если битов меньше чем bit_count
    Возвращает число в двоичной системе счисления если битов больше чем bit_count

    Args:
        number_bit_count (int): число которое мы переводим
        bit_count (int): количество битов в числе
        result_bit_count(str): записываем сюда биты 

    Пример:
        >>>print(convert_to_binary_if(10))
        '0101'

    """
    result_bit_count = []  # тут будет результат, но я не уверен
    
    while number_bit_count > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        result_bit_count.append(number_bit_count % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number_bit_count //= 2  # магия. не трогать!!!
        bit_count += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if bit_count > 10:  # 10 взял из головы, потом поменяю (нет)
        result_bit_count.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, result_bit_count)) if result_bit_count else "0"  # FIXME: работает — не трогай

print(convert_to_binary_if(10))
