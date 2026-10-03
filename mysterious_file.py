# Пример


def make_tea(water_ml: int, sugar_spoons: int) -> str:
    """
    Формирует описание чая с указанным количеством воды и сахара.

    Args:
        water_ml (int): Объём воды в миллилитрах.
        sugar_spoons (int): Количество ложек сахара.

    Returns:
        str: Строка с описанием получившегося напитка.

    Example:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"


print(make_tea(200, 2))


# Функция 1


def buy_products(
    money: int,
    price_per_item: int,
    items_count: int
) -> int | str:
    """
    Рассчитывает стоимость покупки и возвращает сдачу.

    Если имеющейся суммы денег недостаточно для покупки,
    функция возвращает сообщение об отсутствии достаточной суммы.

    Args:
        money (int): Количество денег, доступное для покупки.
        price_per_item (int): Цена одного товара.
        items_count (int): Количество покупаемых товаров.

    Returns:
        int | str: Размер сдачи в виде целого числа,
        если денег достаточно, или строку "Недостаточно денег",
        если денег недостаточно.

    Example:
        >>> buy_products(100, 10, 5)
        50

        >>> buy_products(20, 15, 2)
        'Недостаточно денег'
    """
    total_cost = price_per_item * items_count

    if total_cost > money:
        return "Недостаточно денег"

    return money - total_cost


print(buy_products(100, 10, 5))


# Функция 2


def is_weekend(day: str) -> bool:
    """
    Проверяет, является ли указанный день выходным.

    Функция принимает название дня на русском языке,
    переводит его в нижний регистр и проверяет,
    является ли он субботой или воскресеньем.

    Args:
        day (str): Название дня недели.

    Returns:
        bool: True, если день является субботой или воскресеньем,
        иначе False.

    Example:
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
    Проверяет, является ли число чётным.

    Число считается чётным, если при делении на 2
    остаток равен нулю.

    Args:
        number (int): Целое число для проверки.

    Returns:
        bool: True, если число чётное, иначе False.

    Example:
        >>> is_even(10)
        True

        >>> is_even(7)
        False
    """
    return number % 2 == 0


# Функция 4


def get_multiples_of_three(
    start: int,
    stop: int,
    step: int = 1
) -> list[int]:
    """
    Возвращает числа из заданного диапазона, которые делятся на 3.

    Функция перебирает числа от start до stop с указанным шагом
    и добавляет в результат только те числа, которые делятся
    на 3 без остатка.

    Args:
        start (int): Начальное значение диапазона.
        stop (int): Конечное значение диапазона, которое
            не включается в диапазон.
        step (int): Шаг изменения значения при переборе.
            По умолчанию равен 1.

    Returns:
        list[int]: Список чисел из диапазона, кратных 3.

    Example:
        >>> get_multiples_of_three(1, 10)
        [3, 6, 9]

        >>> get_multiples_of_three(1, 15, 2)
        [3, 9]
    """
    multiples = []

    for number in range(start, stop, step):
        if number % 3 == 0:
            multiples.append(number)

    return multiples


# Функция 5


def calculate_sentiment_score(
    text: str,
    positive_words: list[str],
    negative_words: list[str]
) -> float:
    """
    Вычисляет простой показатель тональности текста.

    Функция разбивает текст на слова и изменяет оценку:
    положительное слово увеличивает оценку на 1,
    отрицательное слово уменьшает оценку на 1.
    Если слово заканчивается на '!', текущая оценка
    умножается на 1.5. Если слово заканчивается на '?',
    текущая оценка умножается на 0.3.

    Args:
        text (str): Текст, тональность которого необходимо определить.
        positive_words (list[str]): Список слов, считающихся положительными.
        negative_words (list[str]): Список слов, считающихся отрицательными.

    Returns:
        float: Итоговая оценка тональности, округлённая
        до одного знака после запятой.

    Example:
        >>> calculate_sentiment_score(
        ...     "I love Python!",
        ...     ["love", "like", "enjoy", "adore", "appreciate"],
        ...     ["hate", "dislike", "detest", "antipathy"]
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

        if word.endswith("!"):
            score *= 1.5
        elif word.endswith("?"):
            score *= 0.3

    return round(score, 1)


print(
    calculate_sentiment_score(
        "I love Python!",
        ["love", "like", "enjoy", "adore", "appreciate"],
        ["hate", "dislike", "detest", "antipathy"]
    )
)


# Функция 6


def convert_to_binary(number: int, digit_count: int = 0) -> str:
    """
    Переводит положительное целое число в двоичную строку.

    Функция последовательно получает остатки от деления числа
    на 2 и выполняет целочисленное деление числа на 2.
    Полученные двоичные цифры записываются в строку.
    Если исходное число равно 0, возвращается строка "0".

    Если количество итераций вместе с исходным значением
    digit_count превышает 10, полученные цифры разворачиваются.

    Args:
        number (int): Положительное целое число,
            которое необходимо перевести в двоичную систему.
        digit_count (int): Начальное значение счётчика итераций.
            По умолчанию равно 0.

    Returns:
        str: Двоичное представление числа в виде строки.
        Для числа 0 возвращается строка "0".

    Example:
        >>> convert_to_binary(10)
        '0101'

        >>> convert_to_binary(0)
        '0'
    """
    binary_digits = []

    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        digit_count += 1

    if digit_count > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"


print(convert_to_binary(10))

