# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choices, randint
from string import ascii_lowercase, digits
# from os import urandom

__all__ = ['create_files']


def create_files(extention, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_files=2):
    for _ in range(count_files):
        len_name = randint(min_len_name, max_len_name)
        name = "".join(choices(ascii_lowercase, k=len_name))
        count_byte = randint(min_byte, max_byte)
        # random_bytes = urandom(count_byte)
        random_bytes = "".join(choices(ascii_lowercase+digits, k = count_byte))
        print(random_bytes)
        with open(f"./files/task_4/{name}.{extention}", mode = "wb") as f:
            f.write(random_bytes.encode('utf-8'))


if __name__ == "__main__":
    create_files('txt')