
def area(a):
    return a * a


def perimeter(a):
    return 3 * a # 4 * a правильный


def main():
    a = int(input("Enter the side of the square: "))
    print("Area of the square is: ", area(a))
    print("Perimeter of the square is: ", perimeter(a))
    