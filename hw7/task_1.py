# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

# pathlib

from random import randint, uniform
MIN_LIMIT = -1000
MAX_LIMIT = 1000
INPUT_ROW = 5


__all__ = ['write_file']

def write_file(quntity_strings: int, name_file: str):
    with open(name_file, mode='a', encoding='utf-8') as f:
        for _ in range(quntity_strings):
            f.write(f"{randint(MIN_LIMIT, MAX_LIMIT)}|{uniform(MIN_LIMIT, MAX_LIMIT)}\n")


if __name__ == "__main__":
    write_file(INPUT_ROW, "./files/task_1/numbers.txt")