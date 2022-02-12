x = 0
y = 0

def init(a, b):
    global x
    global y
    x = Fraction(a)
    y = Fraction(b)

from fractions import Fraction

def rational_sum():
    return x+y
    
def rational_minus():
    return x-y

def rational_division():
    return x/y

def rational_multi():
    return x*y
