# Документация к mysterious_file.py

Лабораторная работа №2. doc_562150.

## make_tea(water_ml, sugar_spoons)

Готовит чай, смешивая воду и сахар
Args:
        water_ml (int): объём воды в миллилитрах
        sugar_spoons (int): количество ложек сахара

    Returns:
        str: описание получившегося напитка

    Пример:
        >>> make_tea(200, 2)
        'Чай: 200 мл воды, 2 ложки сахара'

## change(money, price_per_item, items_count)

Подсчитывает сдачу после покупки одинаковых товаров.

Args:
        money (int / float): сколько денег у покупателя
        price_per_item (int / float): цена одной единицы товара
        items_count (int): количество купленных товаров
 
    Returns:
        int /float /str: сдача, либо строка
            "Недостаточно денег", если стоимость покупки больше money

    Пример:
        >>> change(100, 10, 5)
        50
        >>> change(100, 10, 11)
        'Недостаточно денег'

## weekend_check(day)

Проверяет, является ли переданный день выходным. Принимает только значения: "сб", "вс", "суббота", "воскресенье".

Args:
        day (str): название дня недели (сокращённое или полное)
 
    Returns:
        bool: True, если день суббота или воскресенье, иначе False
 
    Пример:
        >>> weekend_check("Суббота")
        True
        >>> weekend_check("пн")
        False

## even(num)

Проверяет, чётное ли число.

Args:
        num (int): целое число для проверки
 
    Returns:
        bool: True, если число делится на 2 без остатка, иначе False
 
    Пример:
        >>> even(4)
        True
        >>> even(7)
        False

## kratno_trem(start, end, step=1)

Возвращает числа из заданного диапазона, которые кратны трём. Число end в диапазон не входит. Шаг step не  равен 0

Args:
        start (int): начало диапазона
        end (int): конец диапазона
        step (int): шаг перебора в диапазоне
 
    Returns:
        list[int]: список чисел, которые кратны 3
 
    Пример:
        >>> kratno_trem(3, 12)
        [3, 6, 9]
        >>> kratno_trem(3, 10, 2)
        [3, 9]

## sentiment_score(text, positive_words, negative_words)

Проверяет настроение текста по списку слов, режет текст по пробелам
Слова из списка positive_words дают по +1, из negative_words -1. При окончании слова на "!",
накопленный счет умножается на 1.5, при окончании на "?" - на 0.3
Слово сравнивается со списком вместе со знаками

Args:
        text (str): анализируемый текст
        positive_words (list[str]): позитивные слова
        negative_words (list[str]): негативные слова
 
    Returns:
        float: счет итого
 
    Пример:
        >>> sentiment_score("I love cats!", ["love"], ["hate"])
        1.5
        >>> sentiment_score("I hate dogs?", ["love"], ["hate"])
        -0.3

## binary(num, bit_counter=0)

Переводит положительное десятичное число в двоичное делением на два.

Args:
        num (int): при num <= 0 вернётся "0"
        bit_counter (int): начальное значение счётчика битов - 0
            Влияет на разворот результата при достижении 10
 
    Returns:
        str: строка из символов '0' и '1'; "0", если num <= 0
 
    Пример:
        >>> to_binary(10)
        '0101'
        >>> to_binary(10, 7)
        '1010'
        >>> to_binary(0)
        '0'

## История изменений ветки doc_562150

bfb16eb docs: rename functions && descriptions
yyyyyyy docs: add markdown documentation 
