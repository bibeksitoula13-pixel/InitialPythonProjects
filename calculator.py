def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by zero")


while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a number")
        continue

    operator = input("Enter operator: ")


    if operator == "+":
        print(add(num1, num2))
    elif operator == "-":
        print(sub(num1, num2))
    elif operator == "*":
        print(mul(num1, num2))
    elif operator == "/":
        print(div(num1, num2))
    else:
        print("Invalid operator")
    usr_choice = input("Do you want to continue? (y/n): ").lower()
    if usr_choice != "y":
        break



