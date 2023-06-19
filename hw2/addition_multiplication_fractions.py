# Задача №2 домашнего задания 2. Сложение и умножение дробей.

from fractions import Fraction


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def fraction_reduction(num, den):
    com_div = gcd(num, den)
    num /= com_div
    den /= com_div
    return int(num), int(den)


def str_split(my_str):
    my_str = my_str.split('/')
    a = int(my_str[0])
    b = int(my_str[1])
    return a, b


def print_fraction(a, b):
    if a % b == 0:
        print(a)
    elif a % b != 0 and a > b:
        print(a // b, '`', a % b, '/', b, sep='')  # приведение к правильной дроби
    else:
        print(a, '/', b, sep='')


str1 = input('введите 1 дробь, в формате a/b: ')
str2 = input('введите 2 дробь, в формате a/b: ')

a1, b1 = str_split(str1)
a2, b2 = str_split(str2)
sum_num = a1 * b2 + a2 * b1
sum_den = b1 * b2
a, b = fraction_reduction(sum_num, sum_den)
print('Результаты "ручного" вычисления дробей:')
print('Сумма дробей:')
print_fraction(a, b)

p_num = a1 * a2
p_den = b1 * b2
a, b = fraction_reduction(p_num, p_den)
print('Произведение дробей:')
print_fraction(a, b)

print('Результаты работы функции Fraction:')
f1 = Fraction(a1, b1)
f2 = Fraction(a2, b2)
print(f1 + f2)
print(f1 * f2)