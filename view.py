from numbers import Rational
import check


def show(data):
    print(f'result = {data}')

def get_value():
    if check.is_complex:
        return complex(input('value = '))
    else:
        return Rational(input('value = '))