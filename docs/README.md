# Документация функций `mysterious_file.py`

Набор из 7 утилитарных функций на Python для обработки строк, чисел и списков 
(подсчета сдачи, проверки выходных, проверки четности, поиск чисел (кратных трем),
оценки тональности текста и перевода числа в двоичную строку).

## Содержание 

- [make_tea](#make_tea)
- [calculate_change](#calculate_change)
- [is_weekend](#is_weekend)
- [is_even](#is_even)
- [find_multiples_of_three](#find_multiples_of_three)
- [calculate_sentiment_score](#calculate_sentiment_score)
- [to_binary_string](#to_binary_string)

## Таблица переименований

| До Изменения | После Изменения | Предназначение |
|--------------|-----------------|----------------|
| `buy_products` | `calculate_change` | считает сдачу |
| `check` | `is_weekend` | проверяет, выходной ли день |
| `h` | `is_even` | проверяет четность |
| `z` | `find_multiples_of_three` | записывает числа, кратные 3 |
| `sentiment_score` | `calculate_sentiment_score` | оценка тональности |
| `f` | `to_binary_string` | переводит число в двоичную сиситему |

---

## make_tea

**Описание:** готовит чай, смешивая воду и сахар.

**Сигнатура:**
```python
make_tea(water_ml, sugar_spoons) -> str
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `water_ml` | `int` | объем воды в миллилитрах |
| `sugar_spoons` | `int` | количество ложек сахара |

**Возвращает:** `str`: Описание получившегося напитка.

**Особенности и подвохи:**
-  «ложки» не склоняется.

**Пример вызова:**
```python
>>> make_tea(200, 2)
'Чай: 200 мл воды, 2 ложки сахара'
```
---

## calculate_change

**Описание:** Вычисляет сдачу при покупке определенного количества товаров.

**Сигнатура:** 
```python
calculate_change(money: int | float, price_per_item: int | float, items_count: int) -> int | float | str
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `money` | `int / float` | сумма денег у клиента |
| `price_per_item` | `int / float` | цена одного товара |
| `item_count` | `int` | количество приобретаемых товаров |

**Возвращает:** `int` | `float` | `str`: Сумма сдачи или сообщение о недостатке средств.

**Особенности и подвохи:**
- результат может быть как числом, так и строкой. 

**Пример вызова:**
```python
>>> calculate_change(100, 10, 5)
50
>>> calculate_change(30, 10, 5)
'Недостаточно денег'
```
---

# is_weekeend

**Описание:** Проверяет, является ли указанный день недели выходным (суббота или воскресенье).

**Сигнатура:** 
```python
is_weekend(day_name: int) -> bool
```
| Параметр | Тип | Описание |
|----------|-----|----------|
| `day_name` | `int` | название дня недели или краткое обозначение |

**Возвращает:** `bool`: True, если день - выходной, иначе False.

**Особенности и подвохи:** 
- возможны только русские названия дней недели.
- пробелы не убираются.

**Пример вызова**
```python
 >>> is_weekend("Суббота")
True
>>> is_weekend("вт")
False
```

---

## is_even

**Описание:** Проверяет, является ли число чётным.

**Сигнатура:**
```python
is_even(number: int) -> bool
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `number` | `int` | проверяемое число, может быть отрицательным |

**Возвращает:** `bool`: `True`, если число делится на 2 без остатка.

**Особенности и подвохи:**
- для `float` тоже работает (`4.0` чётное, `2.5` нет);
- для строки или `None` будет `TypeError`.

**Пример вызова:**
```python
>>> is_even(6)
True
>>> is_even(1)
False
```

---

## find_multiples_of_three

**Описание:** Находит числа, кратные трём, среди чисел от `start` до `stop`
(не включая `stop`) с шагом `step`.

**Сигнатура:**
```python
find_multiples_of_three(start: int, stop: int, step: int = 1) -> list[int]
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `start` | `int` | начало диапазона (включительно) |
| `stop` | `int` | конец диапазона (**не** включительно) |
| `step` | `int` | шаг перебора, по умолчанию `1` |

**Возвращает:** `list[int]` — кратные трём числа в порядке перебора;
пустой список, если таких нет.

**Особенности и подвохи:**
- Ноль кратен трём, поэтому при `start <= 0` он попадёт в список.
- `step=0` вызывает `ValueError`, нецелые аргументы — `TypeError`.

**Примеры вызова:**
```python
>>> find_multiples_of_three(1, 10)
[3, 6, 9]
>>> find_multiples_of_three(1, 20, 2)
[3, 9, 15]
```

---

## calculate_sentiment_score

**Описание:** Оценивает тональность текста одним числом. Больше нуля — текст
позитивный, меньше нуля — негативный.

**Сигнатура:**
```python
calculate_sentiment_score(text: str, positive_words: list[str], negative_words: list[str]) -> int | float
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `text` | `str` | анализируемый текст |
| `positive_words` | `list[str]` | позитивные слова, **в нижнем регистре**, по одному слову |
| `negative_words` | `list[str]` | негативные слова, **в нижнем регистре**, по одному слову |

**Возвращает:** `int` или `float` — итоговый балл, округлённый до одного знака
после запятой. Если в тексте нет слов, оканчивающихся на `!` или `?`, вернётся
`int`, иначе `float`.

**Особенности и подвохи:**
- Знаки препинания не отделяются от слов.
- Результат зависит от порядка слов.
- Фразы из нескольких слов в списках не сработают, так как текст режется по пробелам.
- Если слово есть в обоих списках, оно считается позитивным.

**Примеры вызова:**
```python
>>> pos = ["love", "like"]
>>> neg = ["hate"]
>>> calculate_sentiment_score("I love Python!", pos, neg)
1.5
>>> calculate_sentiment_score("I hate this!", pos, neg)
-1.5
>>> calculate_sentiment_score("Do you like it?", pos, neg)
0.3
```

---

## to_binary_string

**Описание:** Переводит неотрицательное целое число в строку из нулей и единиц,
многократно деля число на 2 и собирая остатки.

**Сигнатура:**
```python
to_binary_string(number: int, min_bits: int = 0) -> str
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| `number` | `int` | число для перевода, ожидается `>= 0` |
| `min_bits` | `int` | начальное значение счётчика битов, по умолчанию `0`. 

**Возвращает:** `str` из символов `0` и `1`. Для `0` и отрицательных чисел
возвращается `'0'`.


**Особенности и подвохи:**
- Остатки собираются от младшего бита к старшему, а правильную запись даёт только разворот, который происходит лишь при `bit_count > 10`. При `min_bits=0` это числа от 1024 (11 бит и больше).
- Для всех меньших чисел биты идут в **обратном** порядке: `to_binary_string(10)` вернёт `'0101'`, а настоящая запись числа 10 — `'1010'`. У чисел-палиндромов (`5` -> `'101'`) разницы не видно, поэтому баг легко пропустить.
- Отрицательные числа не поддерживаются (вернётся `'0'`).

**Примеры вызова:**
```python
>>> to_binary_string(0)
'0'
>>> to_binary_string(10)
'0101'
>>> to_binary_string(6, 8)
'110'
```

---

## История изменений

- `<17a1592>` - Module description implemented.
- `<0b8c98a>` - Function 1. refactor: function 1 renamed and docstrings with doctests added
- `<4912b08>` - Function 2. refactor: function 2 renamed, variable renamed, docstrings with doctests added.
- `<d491271>` - Function 3. refactor: function 3 renamed, variable renamed, docstrings with doctests added.
- `<7d2a692>` - Function 4. refactor: function 4 renamed, variables renamed, docstrings with doctests added.
- `<a4a0d45>` - Function 5. refactor: function 5 renamed, variables renamed, docstrings with doctests added.
- `<8e22759>` - Function 6. refactor: function 6 renamed, variables renamed, docstrings with doctests added.
- `<5983b36>` - Fixed issues in Function 5 and Functions 6. Docstring tests are passed successfuly.
- `<f798fd1>` - Last change of the document. All tests are passed successfully.
- `<45656bc>` - Final commit. Function 5: previous logic change removed. Function 6: variable value changed.
- `<26ac73e>` - Final final commit. Function 6: variable values issue fixed. All docstring tests are passed!
- `<2e952ee>` - Documentation is done. Description, Change Table, Detailed Function descriptions, Changing History are implemented successfully!