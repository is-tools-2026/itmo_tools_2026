def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        b = 1
        for i in range(2, a + 1):
            b *= i
    return b

a = int(input("Enter any number: "))
print(a)