# Задача №1 домашнего задания 2. Конвертер в шестнадцатеричные значения.

DIGIT_NUMBER_SYSTEM = 16


def convert_int_to_hex(number):
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
             8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hex_number = ''
    while number > 0:
        rem = number % DIGIT_NUMBER_SYSTEM
        hex_number = table[rem] + hex_number
        number = number // DIGIT_NUMBER_SYSTEM
    return hex_number

number = int(input('Введите число: '))
print('Результат "ручной" конвертации в шеснадцатеричное занчение: ' + '0x' + convert_int_to_hex(number))
print('Результат работы функции hex: ' + hex(number))