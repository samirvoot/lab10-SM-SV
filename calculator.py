import math
def add(a, b):
    return a + b

def sub(a, b):
   return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        result = b / a
    except ZeroDivisionError:
        print("You can't divide by zero!")
        result = None
    return result

def log(a, b):
    try:
        result = math.log(b, a)
    except ValueError:
        print('Enter valid numbers!')
        result = None
    return result

def exp(a, b):
    return a**b


