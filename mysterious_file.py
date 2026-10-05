# Пример
"""
Набор небольших утилит, оставленных прошлым разработчиком.

Модуль содержит функции для подсчета сдачи, проверки выходных,
проверки четности, поиск чисел (кратных трем), оценки тональности текста и
перевода числа в двоичную строку.

Проверка примеров из документации:
    python -m doctest -v mysterious_file.py
"""


def make_tea(water_ml: int, sugar_spoons: int) -> str:
    """
    Готовит чай, смешивая воду и сахар.

    Args:
        water_ml (int): Объём воды в миллилитрах.
        sugar_spoons (int): Количество ложек сахара.

    Returns:
        str: Описание получившегося напитка.

    Пример:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))

# Функция 1

def calculate_change(money: int | float, price_per_item: int | float, items_count: int) -> int | float | str:
    """
    Вычисляет сдачу при покупке определенного количества товаров.

    Args:
        money (int | float): Сумма денег у клиента.
        price_per_item (int | float): Цена одного товара.
        items_count (int): Количество приобретаемых товаров.

    Returns:
        int | float | str: Сумма сдачи или сообщение о недостатке средств.
    
    Example:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(30, 10, 5)
        'Недостаточно денег'
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(calculate_change(100, 10, 5))

# Функция 2

def is_weekend(day_name: str) -> bool:
    """
    Проверяет, является ли указанный день недели выходным (суббота или воскресенье).

    Args:
        day_name (str): Название дня недели или краткое обозначение.

    Returns:
        bool: True, если день - выходной, иначе False.
    
    Example:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("вт")
        False
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    Args:
        number (int): Проверяемое целое число.

    Returns:
        bool: True, если число четное, иначе False.

    Example:
        >>> is_even(6)
        True
        >>> is_even(1)
        False
    """

    return number % 2 == 0

# Функция 4

def find_multiples_of_three(start: int, stop: int, step: int = 1) -> list[int]:
    """
    Находит все числа, кратные трем, в заданном диапазоне.

    Args:
        start (int): Начало диапазона.
        stop (int): Конец диапазона (не включительно).
        step (int): Шаг итерации (длинна шага), который по умолчанию равен 1.
    
    Returns:
        list[int]: Список чисел из диапазона, которые соответствуют условию кратности 3.

    Example:
        >>> find_multiples_of_three(1, 10)
        [3, 6, 9]
    """
    multiples = []
    for current_number in range(start, stop, step):
        if current_number % 3 == 0:
            multiples.append(current_number)
    return multiples

# Функция 5

def calculate_sentiment_score(text: str, positive_words: list[str], negative_words: list[str]) -> float:
    """
    Оценивает тональность текста на основе списков позитивных или негативных слов.
    Учитывает восклицательные (увеличение эмоционральности) и вопросительные знаки (возникновение неуверенности) в конце слов.

    Args:
        text (str): Входной текст.
        positive_words (list[str]): Список всех слов с позитивным тоном.
        negative_words (list[str]): Список всех слов с негативным тоном.
    
    Returns:
        float: Итоговый бал тональности (округлен до 1 знака после запятой).
    
    Example:
        >>> calculate_sentiment_score("C++ is my favourite coding language!", [favourite, mostly likeable], [worst, disgusting])
        1.5
    """
    
    words = text.lower().split()
    score = 0.0
    
    for word in words:
        clean_word = word.strip("!?.,")
        if clean_word in positive_words:
            score += 1 
        elif clean_word in negative_words:
            score -= 1 
        
        if word.endswith('!'):
            score *= 1.5
        elif word.endswith('?'):
            score *= 0.3 
    
    return round(score, 1)


print(calculate_sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def f(x, y=0):  # TODO: переименовать, Витя опять не согласовал нейминг
    z = []  # тут будет результат, но я не уверен
    
    while x > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        z.append(x % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        x = x // 2  # магия. не трогать!!!
        y += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if y > 10:  # 10 взял из головы, потом поменяю (нет)
        z.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, z)) if z else "0"  # FIXME: работает — не трогай

print(f(10))
