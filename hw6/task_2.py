
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint

__all__ = ['find_number']

_LOWER_LIMIT = 0
_UPPER_LIMIT = 100
_TRY_QUANTITY = 5


def find_number(lower_limit, upper_limit, try_quantity):
    print(f"Я загадаю случайное число в диапазоне от {lower_limit} до {upper_limit}.\nПопробуй его отгадать за {try_quantity} попыток")
    num = randint(lower_limit, upper_limit)
    try_counter = try_quantity
    while try_counter > 0:
        input_data = int(input(f"Осталось {try_counter} попыток. Введите число: "))
        if input_data < lower_limit or input_data > upper_limit:
            print("Неверный ввод!")
        elif num == input_data:
            return True
        elif num > input_data:
            print(f"Больше!")
        else:
            print(f"Меньше!")
        try_counter -= 1
    else:
        print(f"Все попытки исчерпаны. Я загадал число {num}")
    return False

if __name__ == "__main__":
    print(find_number(_LOWER_LIMIT, _UPPER_LIMIT, _TRY_QUANTITY))