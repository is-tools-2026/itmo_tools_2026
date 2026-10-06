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
    Вычисляет сдачу при покупке нескольких одинаковых товаров.

    Args:
        money (int): сумма денег у покупателя
        price_per_item (int): цена одной единицы товара
        items_count (int): количество покупаемых товаров

    Returns:
        int | str: величина сдачи либо строка "Недостаточно денег",
                     если имеющейся суммы не хватает на покупку

    Пример:
        >>> calculate_change(100, 10, 5)
        50
        >>> calculate_change(10, 10, 5)
        'Недостаточно денег'
    """
    total = price_per_item * items_count
    if total > money:
      return "Недостаточно денег"
    return money - total

print(calculate_change(100, 10, 5))

# Функция 2

def is_weekend(day: str) -> bool:
    """
    Определяет, является ли переданный день недели выходным.
    Сравнивает строку в нижнем регистре с набором названий субботы и воскресенья.

    Args:
        day (str): название дня недели (регистр не важен)

    Returns:
        bool: True, если день — суббота или воскресенье, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("Понедельник")
        False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3

def is_even(number: int) -> bool:
    """
    Проверяет, является ли переданное целое число чётным.

    Args:
        number (int): целое число для проверки

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    return number % 2 == 0

# Функция 4

def multiples_of_three_in_range(start: int, end: int, step: int = 1) -> list[int]:
    """
    Возвращает список чисел в диапазоне от start до end (не включая end)
    с заданным шагом, которые делятся на 3 без остатка.

    Args:
        start (int): начало диапазона (включительно)
        end (int): конец диапазона (исключительно)
        step (int, optional): шаг обхода диапазона. По умолчанию 1.

    Returns:
        list[int]: список чисел, кратных 3, из указанного диапазона

    Пример:
        >>> multiples_of_three_in_range(0, 10, 1)
        [0, 3, 6, 9]
        >>> multiples_of_three_in_range(1, 20, 2)
        [3, 9, 15]
    """
    result = []
    for i in range(start, end, step):
        if i % 3 == 0:
            result.append(i)
    return result

# Функция 5

def analyze_sentiment(text: str, positive_words: list[str], negative_words: list[str]) -> float:
    """
    Оценивает эмоциональную тональность текста на основе словарей позитивных
    и негативных слов. Учитывает пунктуацию: восклицательный знак усиливает
    оценку в 1.5 раза, вопросительный — уменьшает до 0.3 от текущей.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных слов
        negative_words (list[str]): список негативных слов

    Returns:
        float: итоговая оценка тональности, округлённая до одной цифры после запятой

    Пример:
        >>> analyze_sentiment(
        ...     "I love Python!",
        ...     ["love", "like"],
        ...     ["hate", "dislike"]
        ... )
        1.5
    """
    words = text.lower().split()
    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

        if word.endswith('!'):
            score *= 1.5
        elif word.endswith('?'):
            score *= 0.3

    return round(score, 1)


print(analyze_sentiment("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def to_binary_reversed(number: int, threshold: int = 0) -> str:
    """
    Преобразует целое неотрицательное число в его двоичное представление
    в виде строки. Если количество битов результата превышает 10,
    строка возвращается в обратном порядке.

    Args:
        number (int): исходное неотрицательное целое число
        threshold (int, optional): служебный параметр (счётчик битов).
                                   По умолчанию 0.

    Returns:
        str: строка с двоичным представлением числа (или его реверсом,
             если длина больше 10), либо "0" для нуля

    Пример:
        >>> to_binary_reversed(10)
        '0101'
        >>> to_binary_reversed(2048)
        '100000000000'
    """
    bits = []

    while number > 0:
        bits.append(number % 2)
        number = number // 2
        threshold += 1

    if threshold > 10:
        bits.reverse()

    return ''.join(map(str, bits)) if bits else "0"

print(to_binary_reversed(10))
