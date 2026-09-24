def area(a, h):
 return a * h / 2

def perimeter(a, b, c):
 return a + b + c

 def main():
    a = int(input("Enter the side of the triangle: "))
    b = int(input("Enter the side of the triangle: "))
    c = int(input("Enter the side of the triangle: "))
    h = int(input("Enter the height of the triangle: "))
    print("Area of the triangle is: ", area(a))
    print("Perimeter of the triangle is: ", perimeter(a))
    