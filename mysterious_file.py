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
    Вычисляет сдачу при оплате товара или сообщает о нехватке денежных средств.

    Args:
        money(int): Сумма денежных средств у покупателя.
        price_per_item(int): Цена за единицу товара.
        items_count(int): Количество оплачиваемых товаров.

    Returns:
        float | srt: Сумма сдачи (float), если денежных средств достаточно,  или строка "Недостаточно денег" (str).
        """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def weekends(day):
    """
    Проверка, является ли введенный день недели выходным

    Args:
        day (str): Название дня недели или его аббревиатура.
    Returns:
        bool: True - указанный день является выходным, False - не является выходным днем.
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(weekends("Суббота"))

# Функция 3

def division(number):
    """
    Проверка числа на четность (делится на 2 без остатка).

    Args:
        number (int): Проверяемое число.
    Returns:
        bool: True - четное, False - нечетное.
    """
    return number % 2 == 0

# Функция 4

def division_by_tree(start, finish, step=1):
    """
    Проверяем, кратно ли число 3 (делится без остатка) в заданном диапазоне.

    Args:
        start (int): Первое число из диапазона.
        finish (int): Последнее число из диапазона.
        step (int): Шаг генерации чисел (по умолчанию равен 1).

    Returns:
        list [int]: Список чисел из диапазона, которые делятся без остатка на 3.
    """
    answer = []
    for i in range(start, finish, step):
        if i % 3 == 0:
            answer.append(i)
    return answer

# Функция 5

def sentiment_analyze(text, positive_words, negative_words):
    """
    Определяет эмоциональную окраску текста на основе ключевых слов.

    Args:
        text(str): Исходный текст для анализа.
        positive_words(list[str] | set[str]): Список слов с позитивной окраской.
        negative_words(list[str] | set[str]): Список слов с негативной окраской.
    Returns:
        float: Итоговый балл окраски текста (округлен до знака поле занятой).
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


print(sentiment_analyze("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def binary(number, bit_count=0):
    """
    Перевод числа в двоичную систему счисления (с ограничениями по ТЗ).

    Args:
        number (int): Десятичное число для перевода.
        bit_count (int): Начальное значение счетчика бит (по умолчанию 0).

    Returns:
        str: Строка с двоичным кодом числа.
    """
    binary_digits  = []
    
    while number > 0:
        binary_digits .append(number % 2)
        number = number // 2
        bit_count += 1
    if bit_count > 10:
        binary_digits .reverse()
    return ''.join(map(str, binary_digits )) if binary_digits  else "0"

print(binary(10))
