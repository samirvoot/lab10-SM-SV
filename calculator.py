import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        print(f"Error in square_root")
        return None

def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b

def sub(a, b):
   return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        result = b / a
    except ZeroDivisionError:
        print("You can't divide by zero!")
        result = None
    return result

def log(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError
        result = math.log(b, a)
    except ValueError:
        print("Cannot compute with negative number.")
        result = None
    return result

def exp(a, b):
    return a**b


