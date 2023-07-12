# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.


from random import randint
from typing import Callable
from functools import wraps


MIN_LEVEL_NUM = 1
MAX_LEVEL_NUM = 100
MIN_LEVEL_TRY = 1
MAN_LEVEL_TRY = 10


def control_game(function_game: Callable):
    @wraps(function_game)
    def wrapper(num, attempts):
        if num not in range(MIN_LEVEL_NUM, MAX_LEVEL_NUM+1):
            num = randint(MIN_LEVEL_NUM, MAX_LEVEL_NUM)
            print("Передаваемое число вне диапазона [1, 100]")
        if attempts not in range(MIN_LEVEL_TRY, MAN_LEVEL_TRY+1):
            attempts = randint(MIN_LEVEL_TRY, MAN_LEVEL_TRY)
            print("Передаваемое число попыток вне диапазона [1, 10]")
        return function_game(num, attempts)
    return wrapper

@control_game
def guess_number(num, quantity_try):
    """Игра-угадайка. Необходимо ввести загадываемое число
    и количество попыток его угадывания"""
    print(
        f"Я загадаю случайное число.\nПопробуй его отгадать за {quantity_try} попыток")
    try_counter = quantity_try
    while try_counter > 0:
        input_data = int(input(f"Осталось {try_counter} попыток. Введите число: "))
        if input_data == num:
            print(f"Верно! Я загадал число {input_data}")
            return True
        elif input_data > num:
            print("Меньше!")
        else:
            print("Больше!")
        try_counter -= 1
    else:
        print(f"Все попытки исчерпаны. Я загадал число {num}")
        return False


if __name__ == "__main__":
    number = 100
    quantity = 11
    # control = control_game(guess_number)
    # control(number, quantity)
    # control_game(guess_number)(number, quantity)
    guess_number(number, quantity)

    guess_number.__name__
    help(guess_number)