def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print(add(a, b))
elif operator == "-":
    print(subtract(a, b))
elif operator == "*":
    print(multiply(a, b))
elif operator == "/":
    print(divide(a, b))
