# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.


from typing import Callable
from functools import wraps


COUNT = 9


def count(num: int = COUNT):
    def deco(function_: Callable):
        list_attempts = []
        @wraps(function_)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                list_attempts.append(function_(*args, **kwargs))
            return list_attempts
        return wrapper
    return deco

@count(COUNT)
def any_function(*args, **kwargs):
    """Функция-ниочёмка"""
    return args, kwargs

if __name__ == "__main__":
    print(any_function("Hello world!", k = 9))
    print(any_function.__name__)
    print(count.__name__)
    help(any_function)