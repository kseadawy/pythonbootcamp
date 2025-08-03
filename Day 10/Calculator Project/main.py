def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


keys = {"+": add, "-": subtract, "*": multiply, "/": divide}
res = 0
again = 'n'
while True:
    if  again == 'n':
        num1 = float(input("What's the first number?:  "))
    else:
        num1 = res
    for key in keys:
        print(key)
    opr = input("Pick an operation: ")

    num2 = float(input("What's the next number?:  "))

    res = keys[opr](num1, num2)
    print(f"{num1} {opr} {num2} = {res}")

    again = input(f"Type 'y' to continue with {res}, type 'n' to start new calculation:")

