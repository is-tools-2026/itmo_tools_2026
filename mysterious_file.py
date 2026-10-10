# Пример оставлен без изменений, он уже задокументирован корректно
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
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))


# Функция 1: Здесь имена были нормальными, просто добавляем документацию
def calculate_change(money, price_per_item, items_count):
    """
    Рассчитывает сдачу после покупки товаров.

    Args:
        money (int/float): имеющаяся сумма денег
        price_per_item (int/float): цена за одну единицу товара
        items_count (int): количество покупаемого товара

    Returns:
        int/float/str: размер сдачи или сообщение о нехватке средств
    """
    total = price_per_item * items_count
    if total > money:
        return "Недостаточно денег"
    return money - total

print(calculate_change(100, 10, 5))


# Функция 2: Переименовываем функцию и аргумент для понятности
def is_weekend(day_name):
    """
    Проверяет, является ли переданный день недели выходным.

    Args:
        day_name (str): название или сокращение дня недели

    Returns:
        bool: True, если это суббота или воскресенье, иначе False
    """
    return day_name.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(is_weekend("Суббота"))


# Функция 3: Переименовываем загадочные h и x
def is_even(number):
    """
    Проверяет число на четность.

    Args:
        number (int): число для проверки

    Returns:
        bool: True, если число четное, иначе False
    """
    return number % 2 == 0


# Функция 4: Даем понятные имена функции и переменным цикла
def get_multiples_of_three(start, end, step=1):
    """
    Возвращает список чисел в заданном диапазоне, кратных трем.

    Args:
        start (int): начало диапазона
        end (int): конец диапазона (не включительно)
        step (int): шаг цикла (по умолчанию 1)

    Returns:
        list: список чисел, которые делятся на 3 без остатка
    """
    result = []
    for i in range(start, end, step):
        if i % 3 == 0:
            result.append(i)
    return result


# Функция 5: Расшифровываем t, p_w, n_w
def sentiment_score(text, positive_words, negative_words):
    """
    Анализирует текст и вычисляет его эмоциональный окрас на основе списков слов и пунктуации.

    Args:
        text (str): анализируемый текст
        positive_words (list): список позитивных слов
        negative_words (list): список негативных слов

    Returns:
        float: итоговый балл настроения текста
    """
    words = text.lower().split()
    score = 0
    
    for word in words:
        # Убираем знаки препинания для корректного поиска в списках
        clean_word = word.rstrip('!?.,') 
        
        if clean_word in positive_words:
            score += 1
        elif clean_word in negative_words:
            score -= 1
        
        if word.endswith('!'):
            score *= 1.5
        elif word.endswith('?'):
            score *= 0.3
            
    return round(score, 1)

print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))


# Функция 6: Магический алгоритм Дмитрия, судя по логике, это перевод в двоичную систему, но в обратном порядке (с костылем)
def custom_to_binary(number, iterations=0):
    """
    Преобразует десятичное число в строку с двоичным представлением 
    (записанным в обратном порядке, с особым условием разворота).

    Args:
        number (int): исходное десятичное число
        iterations (int): счетчик итераций (по умолчанию 0)

    Returns:
        str: строковое представление результата
    """
    binary_digits = []
    
    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
        iterations += 1
        
    if iterations > 10:
        binary_digits.reverse()
        
    return ''.join(map(str, binary_digits)) if binary_digits else "0"

print(custom_to_binary(10))