# from operations import add, divide, multiply, power, subtract
#
# from Defining Classes.math_operations.operations import add, divide, multiply, power, subtract

def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def power(x, y):
    return x ** y


def calculate_expression(expression):
    (x, sign, y) = expression.split(' ')
    x = float(x)
    y = int(y)
    if sign == '+':
        result = add(x, y)
    elif sign == '-':
        result = subtract(x, y)
    elif sign == '*':
        result = multiply(x, y)
    elif sign == '/':
        result = divide(x, y)
    elif sign == '^':
        result = power(x, y)
    else:
        raise Exception(f'Invalid sign {sign}')
    return f'{result:.2f}'


expression = input()
print(calculate_expression(expression))
