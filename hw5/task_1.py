# Задача №1 домашнего задания 5. Разбор пути к файлу.

from pathlib import Path


def path_parse(path_str):
    fale_name = Path(path_str).name
    name = Path(path_str).stem
    way = path_str.replace(fale_name, '')
    file_extension = fale_name.replace(name + '.', '')
    return way, name, file_extension


path_str = 'C:/User/folder/fale.txt'
print(path_parse(path_str))