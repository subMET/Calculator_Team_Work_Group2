from email.mime import image


def is_complex(value):
    return (isinstance(value, complex) and (value.imag != 0))