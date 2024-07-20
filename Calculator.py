
def takeinput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    calculate(num1, num2)


def calculate(num1, num2):
    global result
    operator = input("Enter an operator ( + - * /): ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    printfunction(result)


def printfunction(result):
    print(round(result, 4))


takeinput()
