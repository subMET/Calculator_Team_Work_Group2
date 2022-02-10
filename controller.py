import view
import complex


def button_click():
    value_a = view.get_value_complex()
    value_b = view.get_value_complex()
    complex.init(value_a, value_b)
    result = complex.complex_sum()
    view.show(result)
