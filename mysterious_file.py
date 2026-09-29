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
    return f"Чай: {water_ml} мл воды, {sugar_spoons} ложки сахара"

print(make_tea(200, 2))

# Функция 1

def give_change(payment, price_per_item, items_count):
    """
    считает и выдает сдачу к покупке.
    args:
        payment (int) - сумма к оплате 
        price_per_item(int) - цена за один товар 
        items_count(int) - кол-во товаров
    returns:
        str: "недостаточно средств" 
        int: сумма сдачи 
    example:
        give_change100,10,5)

    """
    price_total = price_per_item * items_count
    if price_total > payment:
        
        return "Недостаточно средств"
    return payment - price_total
print(give_change(100, 10, 5))




# Функция 2

def check_is_day_weekend(d):
    """
    функция проверяет, является ли день выходным
    args:
        d (str) - день недели 
    return:
        bool: true/false 
    example :
        check_is_day_weekend("пятница")
    """
    
    return d.lower() in ["сб", "вс", "суббота", "воскресенье"]

print(check_is_day_weekend("Суббота"))

# Функция 3

def chetnost(x):
    """
    функция проверяет число на четность
    args: 
        x (int) - входное число
    returns:
        bool - true/false 
    example:
        chetnost(4)

    """
    return x % 2 == 0

# Функция 4

def tolko_kratnye_3(a, b, c=1):
   """
   функция проееряет какие числа в диапозоне от а до b кратны трем 
   args:
        a  (int) - первое число
        b (int) - второе число
        c (int) - шаг цикла, сколько раз числа проверяются и добовляются в список, по умолчанию 1 
    returns:
        r (list) -  список из чисел краных 3
    example:
        tolko_kratnye_3(3,8)
   
   """
   r = []
   for i in range(a, b, c):
        if i % 3 == 0:
            r.append(i)
        return r

# Функция 5

def sentiment_score(text,positive_words  , negative_words ):
    """"
    функция определяет эмоциональный окрас текста по ключевым словам: 
    анализируемый текст разбивается по пробелам на слова,так-же проверяются символы на которые кончается предложение, и в зависимости от принадлежености
    этих слов к списку плохих и хороших слов, тексту выдается оценка в виде числа 
    args:
        text (str) - входящий текст
        positive_words (list) - список позитивных слов
        negative_words (list) - список негативных слов 
    returns:
        score (float/int) - итоговый балл по котрому оценивается эмоциональный окрас текста
    example:
        sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"])

    """
    words = text.lower().split()
    score = 0
    
    for word in words:
        if word in positive_words :
            score += 1 
        elif word in negative_words :
            score -= 1  
        
        if word.endswith('!'):
            score *= 1.5  
        elif word.endswith('?'):
            score *= 0.3  
    
    return round(score, 1)


print(sentiment_score("I love Python!", ["love", "like", "enjoy", "adore", "appreciate"], ["hate", "dislike", "detest", "antipathy"]))

# Функция 6

def per_bin(number, operation_count=0):   
   
    """
    делит число на 2 и сохраняет остатки от деления.
    Если operation_count > 10, разворачивает порядок остатков.
    args: 
        number (int) изначальное число
        operation_count(int) счетчик кол-ва раз которое функция совершит деление числа на 2
    return:
        ostatki (str) - остатки от деления числа числа как строка, если operation_count >10 
        то возвращает развернутую строку 
    example: per_bin(10)

    
    """
    ostatki = [] 
    
    while number > 0: 
        ostatki.append(number % 2)  
        number = number // 2  
        operation_count += 1  
    if operation_count > 10:  
        ostatki.reverse()  
    return ''.join(map(str, ostatki)) if ostatki else "0"  

print(per_bin(10))
