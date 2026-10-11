Описание функций
make_tea(water_ml, sugar_spoons)

Готовит чай: собирает строку из количества воды и сахара.

Args:

water_ml (int): объём воды в миллилитрах
sugar_spoons (int): количество ложек сахара

Returns:

str: описание напитка

Пример:

python
make_tea(200, 2)  # 'Чай: 200 мл воды, 2 ложки сахара'
calculate_change(money, price_per_item, items_count)

Считает сдачу после покупки. Если денег не хватает, возвращает текст.

Args:

money (int | float): сколько денег есть
price_per_item (int | float): цена одного товара
items_count (int): сколько товаров покупаем

Returns:

int | float | str: сдача или строка "Недостаточно денег"

Пример:

python
calculate_change(100, 10, 5)  # 50
calculate_change(20, 10, 5)   # 'Недостаточно денег'
is_weekend(day_name)

Проверяет, выходной ли день ("сб", "вс", "суббота", "воскресенье"). Регистр не важен.

Args:

day_name (str): название дня недели на русском

Returns:

bool: True, если выходной, иначе False

Пример:

python
is_weekend("Суббота")  # True
is_weekend("пн")       # False
is_even(number)

Проверяет, чётное ли число.

Args:

number (int): проверяемое число

Returns:

bool: True, если число чётное

Пример:

python
is_even(4)  # True
is_even(7)  # False
get_multiples_of_three(start, stop, step=1)

Возвращает числа из диапазона, которые делятся на 3. Число stop не входит в диапазон.

Args:

start (int): с какого числа начинать
stop (int): на каком числе остановиться (не включая его)
step (int): шаг, по умолчанию 1

Returns:

list[int]: список чисел, кратных 3

Пример:

python
get_multiples_of_three(1, 20)  # [3, 6, 9, 12, 15, 18]
sentiment_score(text, positive_words, negative_words)

Оценивает настроение текста. Позитивное слово даёт +1, негативное -1. Слово с "!" на конце умножает счёт на 1.5, с "?" на 0.3. Слова со знаками препинания ("love!") в списки не попадают.

Args:

text (str): текст
positive_words (list[str]): список позитивных слов
negative_words (list[str]): список негативных слов

Returns:

float: итоговый счёт, округлённый до 1 знака

Пример:

python
sentiment_score("I love Python!", ["love"], ["hate"])  # 1.5
decimal_to_binary(number, bit_counter=0)

Переводит число в двоичную запись (строкой). Особенность: для чисел меньше 1024 цифры получаются в обратном порядке, например для 10 вернётся '0101', а не '1010'.

Args:

number (int): число для перевода
bit_counter (int): начальное значение счётчика цифр, по умолчанию 0

Returns:

str: двоичная запись числа

Пример:

python
decimal_to_binary(10)    # '0101'
decimal_to_binary(1024)  # '10000000000'
История изменений ветки doc_561924
a4f8e33 начальная точка (состояние main)
332625e Add docstrings and rename functions in mysterious_file.py