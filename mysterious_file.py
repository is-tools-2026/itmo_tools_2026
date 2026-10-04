from typing import List, Union, Iterable


def make_tea(water_ml: int, sugar_spoons: int) -> str:
    """
    Готовит чай, смешивая воду и сахар.

    Args:
        water_ml (int): объём воды в миллилитрах
        sugar_spoons (int): количество ложек сахара

    Returns:
        str: описание получившегося напитка

    Особенности:
        Слово «ложки» не склоняется: для 1 или 5 ложек текст
        будет грамматически неверным.

    Пример:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'
    """
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"


def buy_products(money: Union[int, float],
                 price_per_item: Union[int, float],
                 items_count: int) -> Union[int, float, str]:
    """
    Считает сдачу после покупки нескольких одинаковых товаров.

    Args:
        money (int | float): сколько денег у покупателя
        price_per_item (int | float): цена одного товара
        items_count (int): количество товаров

    Returns:
        int | float: сдача (money - стоимость), если денег хватает
            (в том числе 0, если сумма равна стоимости);
        str: строка "Недостаточно денег", если стоимость больше money

    Особенности:
        Налоги не учитываются.

    Пример:
        >>> buy_products(100, 10, 5)
        50
        >>> buy_products(100, 30, 5)
        'Недостаточно денег'
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total


def is_weekend(day_name: str) -> bool:
    """
    Проверяет, является ли день недели выходным.

    Args:
        day_name (str): название дня: "сб", "вс", "суббота" или
            "воскресенье" в любом регистре

    Returns:
        bool: True для субботы и воскресенья, иначе False

    Особенности:
        Пробелы по краям не обрезаются: " суббота" вернёт False.
        Английские названия (Saturday) не распознаются.

    Пример:
        >>> is_weekend("Суббота")
        True
        >>> is_weekend("пн")
        False
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]


def is_even(number: int) -> bool:
    """
    Проверяет, является ли число чётным.

    Args:
        number (int): проверяемое число

    Returns:
        bool: True, если число делится на 2 без остатка, иначе False

    Пример:
        >>> is_even(10)
        True
        >>> is_even(7)
        False
    """
    return number % 2 == 0


def filter_multiples_of_three(start: int, stop: int, step: int = 1) -> List[int]:
    """
    Возвращает числа из range(start, stop, step), кратные трём.

    Args:
        start (int): начало диапазона (включительно)
        stop (int): конец диапазона (не включается)
        step (int): шаг перебора, по умолчанию 1; не может быть 0
            (будет ValueError). Это шаг обхода диапазона, а не
            кратность: кратность всегда равна трём.

    Returns:
        list[int]: найденные числа в порядке обхода диапазона;
            пустой список, если подходящих нет

    Особенности:
        Число 0 считается кратным трём и попадёт в результат,
        если входит в диапазон. Отрицательный шаг работает, если
        start > stop.

    Пример:
        >>> filter_multiples_of_three(1, 20)
        [3, 6, 9, 12, 15, 18]
        >>> filter_multiples_of_three(0, 10, 2)
        [0, 6]
        >>> filter_multiples_of_three(10, 0, -1)
        [9, 6, 3]
    """
    result = []
    for number in range(start, stop, step):
        if number % 3 == 0:
            result.append(number)
    return result


def sentiment_score(text: str,
                    positive_words: Iterable[str],
                    negative_words: Iterable[str]) -> Union[int, float]:
    """
    Оценивает тональность текста по словарям позитивных и негативных слов.

    Алгоритм: текст приводится к нижнему регистру и делится по пробелам.
    Для каждого слова по порядку:
      1. слово из positive_words: счёт +1; иначе из negative_words: счёт -1;
      2. если слово оканчивается на "!", весь текущий счёт умножается на 1.5;
         если на "?", весь текущий счёт умножается на 0.3.

    Args:
        text (str): анализируемый текст
        positive_words (Iterable[str]): позитивные слова в нижнем регистре
        negative_words (Iterable[str]): негативные слова в нижнем регистре

    Returns:
        int | float: итоговый счёт, округлённый до 1 знака. Положительный
            означает позитивный текст, отрицательный негативный, 0 нейтральный.

    Особенности:
        - Множитель за "!" и "?" применяется ко всему накопленному счёту,
          а не к одному слову, поэтому результат зависит от порядка слов.
        - Знаки препинания не отделяются: "love!" не найдётся в словаре
          (слово целиком "love!"), но множитель 1.5 всё равно сработает.
        - Если слово есть в обоих списках, учитывается как позитивное.
        - Без множителей результат целый (int), с ними вещественный (float).

    Пример:
        >>> sentiment_score("I love Python!", ["love", "like"], ["hate"])
        1.5
        >>> sentiment_score("I hate this", ["love"], ["hate"])
        -1
        >>> sentiment_score("Do you like it?", ["like"], ["hate"])
        0.3
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


def int_to_binary_string(number: int, initial_count: int = 0) -> str:
    """
    Переводит неотрицательное целое число в строку из нулей и единиц.

    Число делится на 2 с остатком, остатки собираются в список (от младшего
    бита к старшему). Счётчик initial_count увеличивается на 1 за каждый бит.
    Если после цикла счётчик больше 10, список разворачивается.

    Args:
        number (int): число для перевода; значения <= 0 дают "0"
        initial_count (int): начальное значение счётчика битов, по умолчанию 0;
            смещает порог разворота (см. «Особенности»)

    Returns:
        str: строка из символов "0" и "1"

    Особенности:
        ВАЖНО: порядок битов зависит от длины числа.
        - Если initial_count + количество_бит <= 10 (для чисел меньше 1024
          при initial_count=0), биты идут от младшего к старшему,
          т.е. строка записана НАОБОРОТ относительно обычной двоичной записи.
        - Если больше 10, список разворачивается и запись правильная.
        Для корректного результата при любом числе используйте bin(number)[2:].
        Число 0 и отрицательные числа возвращают "0" без ошибки.

    Пример:
        >>> int_to_binary_string(10)
        '0101'
        >>> int_to_binary_string(1024)
        '10000000000'
        >>> int_to_binary_string(0)
        '0'
    """
    bits = []
    count = initial_count

    while number > 0:
        bits.append(number % 2)
        number = number // 2
        count += 1
    if count > 10:
        bits.reverse()
    return ''.join(map(str, bits)) if bits else "0"


if __name__ == "__main__":
    print(make_tea(200, 2))
    print(buy_products(100, 10, 5))
    print(is_weekend("Суббота"))
    print(is_even(10))
    print(filter_multiples_of_three(1, 20))
    print(sentiment_score(
        "I love Python!",
        ["love", "like", "enjoy", "adore", "appreciate"],
        ["hate", "dislike", "detest", "antipathy"],
    ))
    print(int_to_binary_string(10))
