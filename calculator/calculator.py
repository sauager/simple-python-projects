import sys


def add(a:int | float, b: int | float):
    return a + b

def subtract(a:int | float, b: int | float):
    return a - b

def division(a:int | float, b: int | float):
    if b != 0:
        return a / b
    raise ValueError('Division by zero is unsupported! Choose a right value')

def multiply(a:int | float, b: int | float):
    return a * b

print("Hi, it's simple python calculator!")
print("I have some operations")

while True:
    print("1. Addition ")
    print("2. Substraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = (input('Choose one of operations (for example "1" for addiction")\n'))
    if str(choice) not in ['1','2','3','4','5']:
        print("Please, choose a right value\n")
        continue
    choice = int(choice)

    match choice:
        case 1:
            print("choose two numbers")
            try:
                a,b = map(float,input().split())
            except:
                print("Please, choose right values\n")
                continue
            print(f"Addiction result: {add(a,b)}\n")

        case 2:
            print("choose two numbers")
            try:
                a, b = map(float, input().split())
            except:
                print("Please, choose right values\n")
                continue
            print(f"Substraction result: {subtract(a, b)}\n")

        case 3:
            print("choose two numbers")
            try:
                a, b = map(float, input().split())
            except:
                print("Please, choose right values\n")
                continue
            try:
                print(f"Division result: {division(a, b)}\n")
            except ValueError as e:
                print(e)

        case 4:
            print("choose two numbers")
            try:
                a, b = map(float, input().split())
            except:
                print("Please, choose right values\n")
                continue
            print(f"Addiction result: {multiply(a, b)}\n")

        case 5:
            print('It was fun!')
            sys.exit()
