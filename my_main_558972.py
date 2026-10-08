def power(a, n):
    """
    Возводит число a в степень n.
    """
    result = 1

    for _ in range(n):
        result *= a

    return result


a = float(input("Введите число: "))
n = int(input("Введите степень: "))

print("Результат:", power(a, n))