from numbers import Rational


def show(data):
    print(f'result = {data}')

def get_value_complex():
    return complex(input('value = '))

def get_value_ratio():
    return Rational(input('value = '))