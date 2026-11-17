def make_tea(water_ml: int, sugar_spoons: int) -> str:
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


def buy_products(money: int, price_per_item: int, items_count: int) -> int | str:
    """
    Рассчитывает покупку товаров и возвращает сдачу либо сообщение о нехватке средств.

    Args:
    money (int): количество имеющихся денег
    price_per_item (int): цена за единицу товара
    items_count (int): количество покупаемых единиц

    Returns:
    int | str: сумма сдачи или строка "Недостаточно денег"
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total


def is_weekend(day_name: str) -> bool:
    """
    Проверяет, является ли переданный день недели выходным.

    Args:
    day_name (str): название или сокращение дня недели

    Returns:
    bool: True, если выходной, иначе False
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]


def is_even(number: int) -> bool:
    """
    Проверяет, является ли число чётным.

    Args:
    number (int): проверяемое число

    Returns:
    bool: True, если чётное, иначе False
    """
    return number % 2 == 0


def get_multiples_of_three(start: int, end: int, step: int = 1) -> list:
    """
    Генерирует список чисел, кратных трём, в заданном диапазоне.

    Args:
    start (int): начало диапазона
    end (int): конец диапазона
    step (int): шаг генерации (по умолчанию 1)

    Returns:
    list: список чисел, делящихся на 3 без остатка
    """
    result = []
    for i in range(start, end, step):
    if i % 3 == 0:
        result.append(i)
    return result


def sentiment_score(text: str, positive_words: list, negative_words: list) -> float:
    """
    Определяет эмоциональную окраску (тональность) текста.

    Args:
    text (str): анализируемый текст
    positive_words (list): список позитивных слов
    negative_words (list): список негативных слов

    Returns:
    float: итоговый балл тональности текста
    """
    words = text.lower().split()
    score = 0.0

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


def decimal_to_binary(decimal_number: int, counter: int = 0) -> str:
    """
    Переводит целое число в двоичную строку с дополнительной внутренней логикой.

    Args:
    decimal_number (int): исходное число в десятичной системе
    counter (int): счётчик итераций

    Returns:
    str: число в двоичном формате виде строки
    """
    binary_digits = []

    while decimal_number > 0:
        binary_digits.append(decimal_number % 2)
        decimal_number = decimal_number // 2
        counter += 1

    if counter > 10:
        binary_digits.reverse()

    return ''.join(map(str, binary_digits)) if binary_digits else "0"
# Примеры вызовов для проверки
if __name__ == "__main__":
    print(make_tea(200, 2))
    print(buy_products(100, 10, 5))
    print(is_weekend("Суббота"))
    print(is_even(4))
    print(get_multiples_of_three(1, 10))
    print(sentiment_score("I love Python!", ["love", "like"], ["hate"]))
    print(decimal_to_binary(10))
