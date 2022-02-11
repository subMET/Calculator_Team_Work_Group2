import view
import complex
import rational_calc


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    complex.init(value_a, value_b)
    result = complex.complex_multi(value_a, value_b)
    view.show(result)
