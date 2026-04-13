"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return b/a
    except ZeroDivisionError:
        return ("Error: Division by Zero")
def log(a,b):
    try:
        if b == 0:
            raise ValueError
        return math.log(a, b)
    except ValueError:
        return ("Error: Logarithm of 0")
def exp(a,b):
    return a**b

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Error: Cannot take square root of negative numbers")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Error: Logarithm of 0")
    return math.log(b, a)

def exponent(a, b):
    return a ** b



