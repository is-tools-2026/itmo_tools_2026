# # Пример

# def make_tea(water_ml, sugar_spoons):
#     """
#     Готовит чай, смешивая воду и сахар.

#     Args:
#         water_ml (int): объём воды в миллилитрах
#         sugar_spoons (int): количество ложек сахара

#     Returns:
#         str: описание получившегося напитка
#     Пример:
#         >>> make_tea(200, 2)
#         'Чай: 200 мл воды, 2 ложки сахара'
#     """
#     # Рецепт одобрен диетологами, которых никто не спрашивал.
#     return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

# print(make_tea(200, 2))

# # Функция 1

# def bought_products(money, price_per_item, items_count):
#     """
#     Вычитает сумму за покупку одинаковых товаров из общей суммы денег у пользователя 

#     Args:
#         money (int): Число денег у пользоавтель
#         price_per_item (float): Цена одного товара
#         items_count (int): Число одинаковых товаров

#     Returns:
#         int / float: Оставшиеся деньги у пользователя
#         str: В противном случае "Недостаточно денег"
    
#     Example:
#         >>> bought_products(100, 10, 5)
#     50
        
#         >>> bought_products(100, 100, 2)
#     "Недостаточно денег"

#     """
    
#     # Выдаёт сдачу. Налоги не включены: их никто не любит, даже эта функция.
#     total = price_per_item * items_count
#     if total > money:
#         # "Денег нет, но вы держитесь" — философская позиция функции.
#         return "Недостаточно денег"
#     return money - total

# print(bought_products(100, 10, 5))

# Функция 2

def is_in_list(d):
    
    """
    Делает проверку на наличие элемента в списке

    Args:
        d (str): Элемент, наличие которого мы хотим проверить
    
    Returns:
        bool: True - есть элемент, False - нет элемента
    Examples:
        list: ["сб", "вс", "суббота", "воскресенье"]
        >>> is_in_list("Суббота")
    True
        
        >>> is_in_list("С")
    False
    """
    
    # Надо подать прошение на включение Пятницы. 
    return d.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_in_list("Суббота"))

# # Функция 3

# def is_even(parametr):
    
#     """
#     Ф-ция, делающая проверку чётное ли число
    
#     Args:
#         parametr (int): Элемент, который мы хотим проверить
#     Returns:
#         bool: True - Кратно 2, False - не кратно 2
#     Examples:
#         При вызове процедуры возвращает
#         >>> is_even(2)
#     True
    
#         >>> is_even(2)
#     False
#     """
# # tests
#     return parametr % 2 == 0
# print(is_even(2))

# # Функция 4

# def multiples_of_3(prm1, prm2, step = 1):
    
#     """ 
#     Ф-ция возвращает список чисел, кратных 3
    
#     Args:
        
#         prm1(int) - Начало дипазона перебора индексов
        
#         prm2(int) - Конец диапозона перебора индексов
        
#         step(int) - Шаг перебора индексов
#             - Если при вызове ф-ции шаг(step) не обозначаем => 
#                 step = 1
#             - Если при вызове ф-ции шаг(step) обозначаем => 
#                 step = <введённое число>
        
#     Returns:
    
#             list: Список индексов списка чисел, делящихся на 3
        
#     Examples:
    
#     >>> 1) Input: 
#         - multiples_of_3(0, 13)
#        Output: 
#         - [0, 3, 6, 9]
    
#     >>> 2) Input: 
#         - multiples_of_3(0, 13, 2)
#        Output: 
#         - [0, 6, 12]

#     >>> 3) Input: 
#         - multiples_of_3(0, 4, 1)
#        Output: 
#         - [0, 3, 6, 9, 12]
    
#     """
    
#     res = []
#     for i in range(prm1, prm2, step):
#         # Почему именно три? Потому что два уже
#         # занял предыдущий разработчик, а четыре — это уже перебор.
#         if i % 3 == 0:
#             res.append(i)
#     return res

# # tests
# num = int(input()) + 1
# # step = int(input())
# print(multiples_of_3(0, 4, 1))

# # Функция 5

def sentiment_score(t, p_w, n_w):
    # Определяет настроение текста точнее, чем мама по голосу в трубке.
    words = t.lower().split()
    s = 0
    
    for word in words:
        if word in p_w:
            s += 1  # плюс балл за позитив, можно ещё два
        elif word in n_w:
            s -= 1  # минус балл за негатив, грустно стало
        
        if word.endswith('!'):
            s *= 1.5  # КРИЧИМ И РАДУЕМСЯ!!!
        elif word.endswith('?'):
            s *= 0.3  # сомнение — энтузиазм падает, как курс валют
    
    return round(s, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

# def f(x, y=0):  # TODO: переименовать, Витя опять не согласовал нейминг
#     z = []  # тут будет результат, но я не уверен
    
#     while x > 0:  # костыль: если x = 0 падает, но заказчик сказал "и так сойдёт"
#         z.append(x % 2)  # зачем тут mod 2? спросите у прошлого разраба, он уволился
#         x = x // 2  # магия. не трогать!!!
#         y += 1  # счётчик дней, недель, часов? хз, в ТЗ не было
#     if y > 10:  # 10 взял из головы, потом поменяю (нет)
#         z.reverse()  # разворот, потому что иначе клиент жаловался
#     return ''.join(map(str, z)) if z else "0"  # FIXME: работает — не трогай

# print(f(10))
