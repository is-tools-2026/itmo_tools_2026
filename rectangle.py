def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

def main():
    a = int(input("Enter the side of the rectangle: "))
    b = int(input("Enter the side of the rectangle: "))
    print("Area of the rectangle is: ", area(a))
    print("Perimeter of the rectangle is: ", perimeter(a))
    