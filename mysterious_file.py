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

# Функция 1 (ранее buy_products)

def calculate_change(money, price_per_item, items_count):
    """
    Рассчитывает сдачу после покупки товара или возвращает сообщение о нехватке средств.

    Args:
        money (float): количество денег у покупателя
        price_per_item (float): цена за единицу товара
        items_count (int): количество единиц товара

    Returns:
        float | str: оставшиеся деньги (сдача) или строка 'Недостаточно денег'

    Пример:
        >>> calculate_change(100, 10, 5)
        50.0
    """
    total_cost = price_per_item * items_count
    if total_cost > money:
        return "Недостаточно денег"
    return money - total_cost

print(calculate_change(100, 10, 5))

# Функция 2 (ранее check)

def is_weekend(day_name):
    """
    Проверяет, является ли переданный день недели выходным.

    Args:
        day_name (str): название или сокращение дня недели

    Returns:
        bool: True, если день является выходным (суббота/воскресенье), иначе False

    Пример:
        >>> is_weekend("Суббота")
        True
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))

# Функция 3 (была h)
def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): проверяемое целое число

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> is_even(4)
        True
    """
    return number % 2 == 0

# Функция 4 (была z)
def filter_numbers_divisible_by_three(start, end, step = 1):
    """
    Формирует список чисел в заданном диапазоне, которые делятся на 3 без остатка.

    Args:
        start (int): начало диапазона
        end (int): конец диапазона
        step (int): шаг инкремента (по умолчанию 1)

    Returns:
        list[int]: список чисел, кратных трём

    Пример:
        >>> filter_numbers_divisible_by_three(1, 10)
        [3, 6, 9]
    """
    result_list = []
    for current_number in range(start, end, step):
        if current_number % 3 == 0:
            result_list.append(current_number)
    return result_list

# Функция 5 (sentiment_score)
def calculate_sentiment_score(text, positive_words, negative_words):
    """
    Оценивает тональность текста на основе списков позитивных и негативных слов,
    учитывая знаки препинания (восклицательные и вопросительные знаки).

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных ключевых слов
        negative_words (list[str]): список негативных ключевых слов

    Returns:
        float: итоговая оценка тональности текста

    Пример:
        >>> calculate_sentiment_score("I love Python!", ["love"], ["hate"])
        1.5
    """
    words = text.lower().split()
    sentiment_sum = 0.0
    
    for word in words:
        if word in positive_words:
            sentiment_sum += 1
        elif word in negative_words:
            sentiment_sum -= 1
        
        if word.endswith('!'):
            sentiment_sum *= 1.5
        elif word.endswith('?'):
            sentiment_sum *= 0.3
    
    return round(sentiment_sum, 1)

print(calculate_sentiment_score("I love Python!", ["love", "like", "enjoy"], ["hate", "dislike"]))

# Функция 6 (была f)
def decimal_to_binary_string(decimal_number, iteration_counter = 0):
    """
    Конвертирует целое число в двоичную строку с учетом специфической логики разворота.

    Args:
        decimal_number (int): число в десятичной системе
        iteration_counter (int): счетчик итераций (по умолчанию 0)

    Returns:
        str: двоичное представление числа в виде строки

    Пример:
        >>> decimal_to_binary_string(10)
        '1010'
    """
    binary_digits = []
    
    while decimal_number > 0:
        binary_digits.append(decimal_number % 2)
        decimal_number = decimal_number // 2
        iteration_counter += 1
        
    if iteration_counter > 10:
        binary_digits.reverse()
        
    return ''.join(map(str, binary_digits)) if binary_digits else "0"

print(decimal_to_binary_string(10))