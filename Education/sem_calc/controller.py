import model
import view

def button():
    chos = int(input('Natural (1) Complex(2) or Rational (3)'))
    if chos == 1:
        value_1 = view.get_value()
        fun = input('Введите операцию: ')
        value_2 = view.get_value()
    elif chos == 2:
        value_2 = view.get_complex()
        fun = input('Введите операцию: ')
        value_1 = view.get_complex()        
    elif chos == 3:
        value_1 = view.get_rational()
        fun = input('Введите операцию: ')
        value_2 = view.get_rational()
    model.init(value_1, value_2)
    if fun == '+':
        result = model.plus()  
    elif fun == '-':
        result = model.minus()
    elif fun == '/':
        result = model.delen()
    elif fun == '*':
        result = model.mult()
    else:
        print('Введите знак + - / *')

    return view.view_data(result)