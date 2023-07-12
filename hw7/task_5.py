# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits

__all__ = ['create_files_with_ext']


def _create_files(extention, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_files=2):
    for _ in range(count_files):
        len_name = randint(min_len_name, max_len_name)
        name = "".join(choices(ascii_lowercase, k=len_name))
        count_byte = randint(min_byte, max_byte)
        random_bytes = "".join(choices(ascii_lowercase+digits, k=count_byte))
        print(random_bytes)
        with open(f"./files/task_5/{name}.{extention}", mode="wb") as f:
            f.write(random_bytes.encode('utf-8'))


def create_files_with_ext(extintions: dict):
    for ext, count in extintions.items():
        _create_files(ext, count_files=count)


if __name__ == "__main__":
    dict_extentions = {'txt': 4, 'bin': 6, 'csv': 2, 'pdf': 1}
    create_files_with_ext(dict_extentions)