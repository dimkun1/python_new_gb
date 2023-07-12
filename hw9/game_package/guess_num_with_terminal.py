# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from sys import argv
from random import randint
__all__ = ['find_number']


_LOWER_LIMIT = 0
_UPPER_LIMIT = 100
_TRY_QUANTITY = 5


def find_number(lower_limit=_LOWER_LIMIT, upper_limit=_UPPER_LIMIT, try_quantity=_TRY_QUANTITY):
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
    _, *params = argv
    print(find_number(*map(int, params)))