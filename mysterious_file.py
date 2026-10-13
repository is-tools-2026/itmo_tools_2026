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

def change(money, price_per_item, items_count):
    """
    Подсчет сдачи после покупки одинаковых товаров.

    Args:
        money (int / float): сколько денег у покупателя
        price_per_item (int / float): цена одной единицы товара
        items_count (int): количество купленных товаров
 
    Returns:
        int / float / str: сдача, либо строка
            "Недостаточно денег", если стоимость покупки больше money

    Пример:
        >>> change(100, 10, 5)
        50
        >>> change(100, 10, 11)
        'Недостаточно денег'
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(change(100, 10, 5))


# Функция 2

def weekend_check(day):
    """
    Проверяет выходной ли день, который принимает.
    Принимает: "сб", "вс", "суббота", "воскресенье"

    Args:
        day (str): название дня недели (сокращённое или полное)
 
    Returns:
        bool: True, если день суббота или воскресенье, иначе False
 
    Пример:
        >>> weekend_check("Суббота")
        True
        >>> weekend_check("пн")
        False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(weekend_check("Суббота"))


# Функция 3

def even(num):
    """
    Проверяет четное ли число.
 
    Args:
        num (int): целое число для проверки
 
    Returns:
        bool: True, если число делится на 2 без остатка, иначе False
 
    Пример:
        >>> even(4)
        True
        >>> even(7)
        False
    """
    return num % 2 == 0


# Функция 4

def multiples_of_three(start, end, step=1):
    """
    Возвращает числа из заданных, которые кратны трем, end - не часть диапазона.
 
    Args:
        start (int): начало диапазона
        end (int): конец диапазона
        step (int): шаг перебора в диапазоне
 
    Returns:
        list[int]: список чисел, которые кратны 3
 
    Пример:
        >>> multiples_of_three(3, 12)
        [3, 6, 9]
        >>> multiples_of_three(3, 10, 2)
        [3, 9]
    """
    res = []
    for i in range(start, end, step):
        if i % 3 == 0:
            res.append(i)
    return res


# Функция 5

def sentiment_score(text, positive_words, negative_words):
    """
    Проверяет настроение текста по списку слов, режет текст по пробелам.
    Слова из списка positive_words дают по +1, из negative_words -1. При окончании слова на "!",
    накопленный счет умножается на 1.5, при окончании на "?" - на 0.3.
    Слово сравнивается со списком вместе со знаками.
 
    Args:
        text (str): анализируемый текст
        positive_words (list[str]): позитивные слова
        negative_words (list[str]): негативные слова
 
    Returns:
        float: счет итого
 
    Пример:
        >>> sentiment_score("I love cats!", ["love"], ["hate"])
        1.5
        >>> sentiment_score("I hate dogs?", ["love"], ["hate"])
        -0.3
    """
    words = text.lower().split()
    s = 0
    for word in words:
        if word in positive_words:
            s += 1
        elif word in negative_words:
            s -= 1
        if word.endswith('!'):
            s *= 1.5
        elif word.endswith('?'):
            s *= 0.3
    
    return round(s, 1)

print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))


# Функция 6

def to_binary(num, bit_counter=0):
    """
    Переводит положительное десятичное число в двоичное делением на два.

    Args:
        num (int): при num <= 0 вернётся "0"
        bit_counter (int): начальное значение счётчика битов - 0.
            Влияет на разворот результата при достижении 10
 
    Returns:
        str: строка из символов '0' и '1'; "0", если num <= 0
 
    Пример:
        >>> to_binary(10)
        '0101'
        >>> to_binary(10, 7)
        '1010'
        >>> to_binary(0)
        '0'
    """
    bits = []
    
    while num > 0:
        bits.append(num % 2)
        num = num // 2 
        bit_counter += 1 
    if bit_counter > 10:
        bits.reverse()
    return ''.join(map(str, bits)) if bits else "0"

print(to_binary(10))