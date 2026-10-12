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
    Покупает одинаковые товары и возвращает сдачу.

    Args:
        money (int | float): сумма денег у покупателя
        price_per_item (int | float): цена одного товара
        items_count (int): количество покупаемых товаров

    Returns:
        int | float | str: сдача, либо сообщение «Недостаточно денег»

    Пример:
        >>> buy_products(100, 10, 5)
        50
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total_price = price_per_item * items_count
    if total_price > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total_price

print(buy_products(100, 10, 5))

# Функция 2

def is_weekend(day):
    """
    Проверяет, является ли день выходным (суббота или воскресенье).

    Args:
        day (str): название дня недели (короткое или полное)

    Returns:
        bool: True, если день — суббота или воскресенье, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    # Надо подать прошение на включение Пятницы.
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): проверяемое целое число

    Returns:
        bool: True, если число делится на 2 без остатка, иначе False

    Пример:
        >>> is_even(4)
        True
    """
    return number % 2 == 0

# Функция 4

def get_multiples_of_three(start, stop, step=1):
    """
    Собирает числа из диапазона [start, stop), которые делятся на 3.

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включительно)
        step (int): шаг перебора, по умолчанию 1

    Returns:
        list[int]: список чисел, кратных трём

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]
    """
    multiples = []
    for number in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if number % 3 == 0:
            multiples.append(number)
    return multiples

# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Оценивает тональность текста по спискам позитивных и негативных слов.

    Каждое позитивное слово даёт +1, каждое негативное — −1.
    Восклицательный знак усиливает оценку в 1.5 раза,
    вопросительный — ослабляет в 0.3 раза.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных слов
        negative_words (list[str]): список негативных слов

    Returns:
        float: итоговая оценка тональности, округлённая до 1 знака

    Пример:
        >>> sentiment_score(
        ...     "I love Python!",
        ...     ["love", "like", "enjoy", "adore", "appreciate"],
        ...     ["hate", "dislike", "detest", "antipathy"],
        ... )
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

# Функция 6

def decimal_to_binary(number, bit_count=0):
    """
    Переводит неотрицательное целое число в двоичную запись.

    Остатки от деления на 2 собираются от младшего бита к старшему.
    Если количество битов больше 10, цифры разворачиваются
    (старший бит оказывается слева).

    Args:
        number (int): неотрицательное целое число
        bit_count (int): начальное значение счётчика битов, по умолчанию 0

    Returns:
        str: двоичная запись числа; для нуля возвращается «0»

    Пример:
        >>> decimal_to_binary(10)
        '0101'
    """
    bits = []  # тут будет результат, но я не уверен

    while number > 0:  # костыль: если number = 0 падает, но заказчик сказал "и так сойдёт"
        bits.append(number % 2)  # младший бит: остаток от деления на 2
        number = number // 2  # сдвиг числа вправо на один бит
        bit_count += 1  # сколько битов уже собрали
    if bit_count > 10:  # 10 взял из головы, потом поменяю (нет)
        bits.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, bits)) if bits else "0"  # FIXME: работает — не трогай

print(decimal_to_binary(10))
