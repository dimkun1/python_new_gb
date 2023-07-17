# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

from typing import Callable
import json
import os
from functools import wraps

def decor(function_: Callable):
    @wraps(function_)
    def wrapper(*args, **kwargs):
        file = os.getcwd() + "\\files\\" + function_.__name__ + ".json"
        if os.path.exists(file):
            with open(file, 'r', encoding="utf-8") as f:
                params = json.load(f)
        else:
            params = []
        result = function_(*args, **kwargs)
        params.append({"args" : args, "kwargs" : kwargs, "results" : result})
        with open(file, 'w', encoding="utf-8") as f:
            json.dump(params, f, indent=2)
    return wrapper


@decor
def some_function(*args, **kwargs):
    """Функация возвращает список входных позиционны аргументов,
    если их больше одного, а также словарь из ключевых элементов"""
    if len(args) > 1:
        dict_for_return = {}
        for i, item in enumerate(args, start = 1):
            dict_for_return.setdefault(i, item)
        return (dict_for_return, kwargs)
    else:
        return (args, kwargs)

if __name__ == "__main__":
    some_function(1, 4 , "Hello", [1, 8, 8.5], par = "hey", x = 8, lisik = ["list", 5, 0])
    help(some_function)