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
    Вычисляет сдачу после покупки заданного количества товаров
    Если денег недостаточно возвращает сообщение "Недостаточно денег"

    Args:
        money (int,float):количество денег у покупателя
        price_per_item(int,float):цена одного товар
        items_count(int):количество товаров

    Returns:
        int,float,str:сдача или сообщение о недостатке денег

    Пример:
         calculate_change(100, 10, 5)
        50
    """
    total_price = price_per_item * items_count

    if total_price > money:
        return "Недостаточно денег"

    return money - total_price


print(calculate_change(100, 10, 5))

# Функция 2
def is_weekend(day):
    """
    Проверяет является ли указанный день выходным

    Args:
        day(str):название или сокращение дня недели

    Returns:
        bool:True, если день является субботой или воскресеньем
        иначеFalse

    Пример:
        is_weekend("Суббота")
        True
    """
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(is_weekend("Суббота"))

# Функция 3

def del_on_two_or_no(number):
    """
    Проверяет является ли число чётным

    Args:
        number(int):число которое необходимо проверить

    Returns:
        bool:true если число чётное иначе False

    Пример:
        del_on_two_or_no(10)
        True
    """
    return number % 2 == 0


print(del_on_two_or_no(10))

# Функция 4
def find_multiples_of_three(start, stop, step=1):
    """
    Находит числа в заданном диапазоне которые делятся на 3

    Args:
        start(int):начало диапазона
        stop(int):конец диапазона
        step(int):шаг изменения числа

    Returns:
        list:список чисел которые делятся на 3

    Пример:
        find_multiples_of_three(1,10)
        [3, 6, 9]
    """
    result = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            result.append(number)

    return result


print(find_multiples_of_three(1, 10))

# Функция 5
def calculate_sentiment_score(text, positive_words, negative_words):
    """
    Вычисляет оценку настроения текста по позитивным
    и негативным словам

    Args:
        text(str):текст для анализа
        positive_words(list):список позитивных слов
        negative_words(list):список негативных слов

    Returns:
        float:числовая оценка настроения текста

    Пример:
      calculate_sentiment_score("I love Python!",["love","like"],["hate","dislike"])
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
print(calculate_sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))
# Функция 6

def convert_to_binary_with_counter(number, counter=0):
    """
    Получает двоичные остатки числа при последовательном делении на 2
    Если значение счётчика становится больше 10
    полученная последовательность разворачивается

    Args:
        number(int):число которое преобразуется
        counter(int):начальное значение счётчика операций

    Returns:
        str:строка состоящая из двоичных цифр

    Пример:
        convert_to_binary_with_counter(10)
        '0101'
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        counter += 1

    if counter > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(convert_to_binary_with_counter(10))
