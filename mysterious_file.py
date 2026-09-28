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
    Считает остаток денег после покупки товаров.
        Args:
            money (int): сумма денег у покупателя
            price_per_item (int): цена одного товара
            items_count (int): количество товаров

         Returns:
            int: остаток денег, если хватило
            str: сообщение "Недостаточно денег", если суммы не хватает
        Пример:
        >>> buy_products(100, 10, 5)
        50
        """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(buy_products(100, 10, 5))

# Функция 2

def weekend(day):
    """
Проверяет является ли день недели выходным
     Args:
        day (str): назавние дня недели
    Returns : 
        bool: True, если день выходной, иначе False
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]
print(weekend("Суббота"))

# Функция 3

def even(number):
    """
    Проверяет является ли число чётным
        Args : 
            number (int) : число, которое проверяют
        Returns : 
            bool: True, если число чётное, иначе False
    """
    return number % 2 == 0 

# Функция 4

def numbers_divisible_by_3(start, stop, step=1):
    """
    Возвращает числа из диапазона, которые делятся на 3 без остатка
        Args : 
            start (int) : начало диапазона
            stop (int) : конец диапазона
            step (int) : шаг перебора (1)
        Returns :
            list[int] : список чисел из диапазона, кратных 3
    """
    result = []
    for i in range(start, stop, step):
        if i % 3 == 0:
            result.append(i)
    return result

# Функция 5
def sentiment_score(text, positive_words, negative_words):
    """
    # Определяет настроение текста по списку положительных и отрицательных слов
        Args :
            text (str) : анализируемый текст
            positive_words (list[str]): список слов, повышающих оценку
            negative_words (list[str]): список слов, понижающих оценку
        Returns :
            float: итоговая оценка настроения текста (округлённая до 1 знака).
               Восклицательный знак в конце слова усиливает эффект на x1.5,
               вопросительный наоборот ослабляет на x0.3
    """
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

def to_binary(number, bit_count=0):
    """
    Функция переводит число в двоичную запись
        Args : 
            number (int): число для перевода
            bit_count (int): счётчик количества бит, который изначально = 0
        Returns : 
            str : воичное представление числа (при малых числах порядок разрядов может быть перевёрнут)
    """
    result = []  # тут будет результат, но я не уверен
    
    while number > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
        result.append(number % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
        number = number // 2  # магия. не трогать!!!
        bit_count += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
    if bit_count > 10:  # 10 взял из головы, потом поменяю (нет)
        result.reverse()  # разворот, потому что иначе клиент жаловался
    return ''.join(map(str, result)) if result else "0"  # FIXME: работает — не трогай

print(to_binary(10))
