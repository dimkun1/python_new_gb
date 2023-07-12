# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import csv
import json
from functools import wraps
from typing import Callable
from random import randint as rnd


__all__ = ['root_quadratic_equation']


MIN_LIMIT_STRINGS = 100
MAX_LIMIT_STRINGS = 1000
MIN_LIMIT_ROOTS = -100
MAX_LIMIT_ROOTS = 100


def generate_coef_to_csv():
    with open("./les_9/files/generator_hw.csv", 'w', newline="", encoding='utf-8') as f:
        csv_write = csv.writer(f)
        for _ in range(rnd(MIN_LIMIT_STRINGS, MAX_LIMIT_STRINGS)):
            a = rnd(MIN_LIMIT_ROOTS, MAX_LIMIT_ROOTS)
            b = rnd(MIN_LIMIT_ROOTS, MAX_LIMIT_ROOTS)
            c = rnd(MIN_LIMIT_ROOTS, MAX_LIMIT_ROOTS)
            csv_write.writerow([a, b, c])


def decorator_for_save_solution(func: Callable):
    @wraps(func)
    def wrapper(*args):
        file_solution = "./les_9/files/solution_hw.json"
        file_coef = "./les_9/files/generator_hw.csv"
        params = []
        result = func(*args)
        with (
            open(file_solution, 'w', encoding='utf-8') as sol,
            open(file_coef, 'r', newline="", encoding='utf-8') as coef
        ):
            csv_reader = csv.reader(coef)
            key_count = 1
            for in_, out_ in zip(csv_reader, result):
                params.append(
                    {f"Ex_{key_count}": f"Input values: {in_} Roots equation:{out_}"})
                key_count += 1
            json.dump(params, sol, indent=2)
    return wrapper


def decorator_for_solution(func: Callable):
    @wraps(func)
    def wrapper():
        with open("./les_9/files/generator_hw.csv", 'r', newline="", encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            list_solution = []
            for roots in csv_reader:
                res_1, res_2 = func(*map(int, roots))
                list_solution.append((str(res_1), str(res_2)))
        return list_solution
    return wrapper


@decorator_for_save_solution
@decorator_for_solution
def root_quadratic_equation(*args):
    """Фунция для вычилсения квадратного уравнения.
    Корни в генерируются в csv-файле. Решения выводятся в json-файл"""
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if a != 0:
        x_1 = (-b + d ** 0.5) / 2 / a
        x_2 = (-b - d ** 0.5) / 2 / a
    elif b != 0:
        x_1 = x_2 = -c / b
    else:
        x_1 = x_2 = "нет корней"
    return x_1, x_2


if __name__ == "__main__":
    generate_coef_to_csv()
    root_quadratic_equation()
    root_quadratic_equation.__name__
    help(root_quadratic_equation)