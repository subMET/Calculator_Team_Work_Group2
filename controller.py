import view
import complex
import rational_calc
import logger
import check

def data_for_log(a,b,r,symbol):
    data = f'{a} {symbol} {b} = {r}'
    return data

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    if check.is_complex(value_a):
        complex.init(value_a, value_b)
        result = complex.complex_multi(value_a, value_b)
    else:
        rational_calc.init(value_a, value_b)
        result = rational_calc.rational_sum(value_a, value_b)
    view.show(result)
    logger.add_record(data_for_log(value_a,value_b,result,'*'))

