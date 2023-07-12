# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


from random import choice, choices, randint
from string import ascii_lowercase, digits
from os import listdir, mkdir

__all__ = ['create_files_with_ext']


def _create_files(extention, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, count_files=2, directory="./files/task_6/"):
    if not directory.split("/")[-2] in listdir("./files/"):
        mkdir(directory)
    for _ in range(count_files):
        len_name = randint(min_len_name, max_len_name)
        name = "".join(choices(ascii_lowercase, k=len_name))
        if name + "." + extention in listdir(directory):
            name = name + choice(digits)
        count_byte = randint(min_byte, max_byte)
        random_bytes = "".join(choices(ascii_lowercase+digits, k=count_byte))
        with open(f"{directory}{name}.{extention}", mode="wb") as f:
            f.write(random_bytes.encode('utf-8'))


def create_files_with_ext(extintions: dict):
    for ext, count in extintions.items():
        _create_files(ext, count_files=count)


if __name__ == "__main__":
    dict_extentions = {'txt': 4, 'bin': 6, 'csv': 2, 'pdf': 1}
    create_files_with_ext(dict_extentions)