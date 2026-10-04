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

def calculate_change(money, price_per_item, items_count):
    """
    Считает сдачу после покупки одинаковых товаров.

    Args:
        money (int, float): сколько денег у покупателя
        price_per_item (int, float): цена одного товара
        items_count (int): количество товаров

    Returns:
        int | float | str: сдача, а если денег не хватает, то строка
            "Недостаточно денег"

    Пример:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(100, 30, 5)
        'Недостаточно денег'
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total_price = price_per_item * items_count
    if total_price > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total_price

print(calculate_change(100, 10, 5))

# Функция 2

def weekend(day_name):
    """
        Проверяет, является ли день недели выходным.

        Args:
            day_name (str): название или сокращение дня недели на русском

        Returns:
            bool: True для субботы и воскресенья, и False для другого

        Пример:
            >>> weekend("Суббота")
            True
            >>> weekend("пн")
            False
        """
    # Надо подать прошение на включение Пятницы. 
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(weekend("Суббота"))

# Функция 3

def even_number(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): проверяемое число

    Returns:
        bool: True, если число делится на 2 без остатка, иначе False

    Пример:
        >>> even_number(4)
        True
        >>> even_number(7)
        False
    """
    return number % 2 == 0

# Функция 4

def multiples_of_three(start, stop, step=1):
    """
        Возвращает числа из диапазона, которые делятся на 3.

        Args:
            start (int): начало диапазона (включительно)
            stop (int): конец диапазона (не включается)
            step (int): шаг перебора, по умолчанию 1

        Returns:
            list[int]: список чисел, кратных 3 (может быть пустым)

        Пример:
            >>> multiples_of_three(1, 16)
            [3, 6, 9, 12, 15]
            >>> multiples_of_three(-5, 5)
            [-3, 0, 3]
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
    Оценивает настроение текста: больше нуля это позитив, меньше нуля негатив.

    Слово из positive_words даёт +1, из negative_words даёт -1.
    Слово с "!" на конце умножает счёт на 1.5, а с "?" умножает на 0.3.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): позитивные слова в нижнем регистре
        negative_words (list[str]): негативные слова в нижнем регистре

    Returns:
        float | int: итоговая оценка, округлённая до 1 знака

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

# Функция 6

def decimal_to_binary_string(number, counter_start=0):
    """
    Переводит число в двоичную запись (строка из 0 и 1).

    Внимание: для чисел меньше 1024 биты идут задом наперёд (10 даёт '0101').

    Args:
        number (int): переводимое число
        counter_start (int): стартовое значение счётчика бит, по умолчанию 0

    Returns:
        str: строка из символов '0' и '1', для 0 и отрицательных чисел "0"

    Пример:
        >>> decimal_to_binary_string(10)
        '0101'
        >>> decimal_to_binary_string(10, 8)
        '1010'
    """
    bits = []  # остатки от деления на 2, от младшего бита к старшему
    bits_counter = counter_start

    while number > 0:  # для number == 0 цикл не идёт, вернётся "0" (не падает)
        bits.append(number % 2)  # очередной бит числа
        number = number // 2  # отбрасываем младший бит
        bits_counter += 1  # считаем биты (плюс стартовое смещение)
    if bits_counter > 10:  # 10 взято из головы, потом поменяю (нет)
        bits.reverse()  # разворот: старший бит первым
    return ''.join(map(str, bits)) if bits else "0"

print(decimal_to_binary_string(10))