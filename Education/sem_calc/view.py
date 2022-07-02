from fractions import Fraction
import fractions

def view_data(data):
    print(f'Результат = {data}')

def get_value():
    return int(input('value = '))

def get_complex():
    return complex(int(input('value = ')), int(input('value = ')))

def get_rational():
    return Fraction(int(input('value = ')), int(input('value = ')))

# a = Fraction(1, 4)
# b = Fraction(1,4)
# print(a+b)



