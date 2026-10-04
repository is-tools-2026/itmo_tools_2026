# Документация проекта

## Функция  change

Вычисление сдачи после покупки заданного количества товаров 
    Args:
        money(int): сумма денег 
        price_per_item(int):цена за один товар 
        items_count(int): количесво товаров 

    Returns:
        int: сдача после покупки
        str: "Недостаточно денег" , если изначальная сумма денег меньше total
    Пример:
        >>>  change(500, 10, 2)
        480
        >>> change(100, 100, 2)
        'Недостаточно денег'

## Функция  is_a_day_off

Проверяет является ли запрошеный день выходным 
    Args:
        day(str):название дня недели (без учета регистра)
    Returns:
        bool: True, если "сб", "вс", "суббота", "воскресенье"
            False во всех других слуиях 
    Пример:
        >>> is_a_day_off("Суббота")
        True
        >>> is_a_day_off("Пн")
        False

## Функция  even_number

Проверяет является ли число четным 
    Args:
        number(int): число для проверки
    Returns:
        bool: True - четное
            False - нечетное 
    Пример:
        >>> even_number(2)
        True
        >>> even_number(77)
        False

## Функция  numbers_multiples_of_three

Проверяет явлиется ли числ кратным трем, если да, то добавляет в списак 
    Args:
        start(int): начальное число входа в цикл 
        stop(int): конечная граница 
        step(int): шаг в цикле
    Returns:
        list[int]: список чисел, кратных трем 
    Пример:
        >>> numbers_multiples_of_three(1, 10 , 1)
        [3,6,9]

## Функция  sentiment_score

Функция вычисляет настроение через слова и знаки препинания 
    Args:
        text(str): текст для анализа
        positive_words(list[str]): список позитивных слов
        negative_words(list[str]): списое негативных слов
    Returns:
        int или float: оценка настроения 
    Пример:
        >>> sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"] )
        1.5

## Функция  converting_a_number_to_binary

Переводит числа в двоичную систему и в зависимости от количества итераций переворачивает или выводит в прямом порядке
    Args:
        number(int): число для перевода
        score(int): счетчик итераций 
    Returns:
        str:двоичные цифры в обратном порядке , если  счетчик меньше или равнен 10 , иначе в пярмом порядке , для чисел меньших или равных 0 возращает "0"
    Пример:
        >>> converting_a_number_to_binary(10)
        '0101'

## История изменений ветки
