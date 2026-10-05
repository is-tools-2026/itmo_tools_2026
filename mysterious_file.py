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
        money (int | float): сумма денег у покупателя
        price_per_item (int | float): цена одного товара
        items_count (int): количество покупаемых товаров

    Returns:
        int | float | str: сумма сдачи, либо строка "Недостаточно денег",
        если денег не хватает

    Пример:
        >>> calculate_change(100, 10, 5)
        50
    """
    # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
    total = price_per_item * items_count
    if total > money:
        # "Денег нет, но вы держитесь" — философская позиция функции.
        return "Недостаточно денег"
    return money - total


print(calculate_change(100, 10, 5))


# Функция 2


def is_weekend(day):
    """
    Проверяет, является ли указанный день недели выходным.

    Args:
        day (str): название дня недели или его сокращение
            (распознаются только "сб", "вс", "суббота", "воскресенье",
            регистр не важен)

    Returns:
        bool: True, если день выходной, иначе False

    Пример:
        >>> is_weekend("Суббота")
        True

    Замечание:
        Распознаются только русские названия. Строка "Sunday" или
        день с лишними пробелами вернут False.
    """
    # Надо подать прошение на включение Пятницы.
    return day.lower() in ["сб", "вс", "суббота", "воскресенье"]


print(is_weekend("Суббота"))


# Функция 3


def is_even(number):
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): целое число для проверки

    Returns:
        bool: True, если число чётное, иначе False

    Пример:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


# Функция 4


def get_multiples_of_three(start, stop, step=1):
    """
    Возвращает список чисел, кратных трём, из диапазона range(start, stop, step).

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включительно)
        step (int): шаг итерации (по умолчанию 1)

    Returns:
        list[int]: список чисел, кратных 3

    Пример:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]

    Замечание:
        При step больше 1 проверяются только числа, которые попадают
        в range, поэтому часть чисел, кратных 3, может быть пропущена
        (например, get_multiples_of_three(1, 10, 2) не вернёт 6).
    """
    result = []
    for i in range(start, stop, step):
        # Почему именно три? Потому что два уже
        # занял предыдущий разработчик, а четыре — это уже перебор.
        if i % 3 == 0:
            result.append(i)
    return result


# Функция 5


def sentiment_score(text, positive_words, negative_words):
    """
    Вычисляет оценку настроения текста на основе позитивных и негативных слов.

    Args:
        text (str): анализируемый текст
        positive_words (list[str]): список позитивных слов
        negative_words (list[str]): список негативных слов

    Returns:
        float: итоговая оценка настроения (округлена до 1 знака)

    Пример:
        >>> sentiment_score("I love Python!", ["love", "like"], ["hate", "dislike"])
        1.5

    Обнаруженные проблемы:
        1. Множители за "!" (×1.5) и "?" (×0.3) применяются ко всему
           накопленному счёту score, а не только к баллу текущего слова.
           Из-за этого порядок слов сильно влияет на результат:
           sentiment_score("love hello! hate", ...) и
           sentiment_score("hate love hello!", ...) дают разные значения
           (0.5 и 0.0 соответственно), хотя набор слов один и тот же.
        2. Слово со знаком препинания на конце (например, "love!") не
           совпадает ни с одним словом из списков, поэтому не засчитывается
           вообще — срабатывает только множитель.
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


def to_binary(number, counter=0):
    """
    Преобразует целое число в его двоичное представление в виде строки.

    Args:
        number (int): целое число для преобразования
        counter (int): вспомогательный счётчик итераций (по умолчанию 0)

    Returns:
        str: двоичное представление числа (или "0" для нуля)

    Пример:
        >>> to_binary(10)
        '1010'

    Обнаруженные проблемы:
        1. Разворот списка битов (bits.reverse()) выполняется только
           когда counter > 10, то есть фактически только для чисел
           от 1024 и больше. Для меньших чисел результат остаётся
           в неверном порядке — например, to_binary(10) возвращает
           "0101" вместо правильного "1010".
        2. Для отрицательных чисел цикл не выполняется ни разу,
           функция возвращает "0".
        3. Так как counter — обычный параметр функции, а не внутренняя
           переменная, его можно случайно передать извне и получить
           другой (в данном случае случайно верный) результат,
           например to_binary(10, 20).
    """
    bits = []
    while number > 0:
        bits.append(number % 2)
        number = number // 2
        counter += 1
        if counter > 10:
            bits.reverse()
            return ''.join(map(str, bits)) if bits else "0"
    bits.reverse()
    return ''.join(map(str, bits)) if bits else "0"


print(to_binary(10))
