# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
from os import path, walk, getcwd
import argparse
import logging


_FILE_PATH = path.dirname(path.realpath(__file__))+'\\files\\task_6.log'

FORMAT = '{levelname:<4}: {msg}'

logging.basicConfig(format=FORMAT, style='{', filename=_FILE_PATH,
                    filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


FileType = namedtuple(
    'FileType', ['name', 'extension', 'folder_flag', 'parrent_folder'])


def folder_content():
    parser = argparse.ArgumentParser(prog="Работа с содержимым каталога")
    parser.add_argument('-p', metavar='Путь к каталогу', type=str, nargs=1,
                        help='Введите абсолютный или относительный путь к каталогу', default=[getcwd()])
    args = parser.parse_args()
    return _find_content(args.p[0])


def _find_content(fold):
    folder = path.abspath(fold)
    if path.isdir(folder):
        return _folder_extract(folder)
    elif path.isfile(folder):
        logger.warning(f'По адресу {folder} находится файл!')
        return f'По адресу {folder} находится файл!'
    elif path.exists(folder) == False:
        logger.error(f'Каталога {folder} не существует!')
        return f'Каталога {folder} не существует!'


def _folder_extract(folder):
    list_of_files = []
    for i, params in enumerate(walk(folder), start=1):
        path_folder, folders, files = params
        for j, item in enumerate(folders + files, start=1):
            abs_path = path.join(path_folder, item)
            if path.isfile(abs_path):
                name = ".".join(item.split(".")[:-1])
                extension = item.split(".")[-1]
                folder_flag = False
            elif path.isdir(abs_path):
                name = item
                extension = "is_folder"
                folder_flag = True
            parrent_folder = abs_path.split('\\')[-2]
            temp_ = FileType(name, extension, folder_flag, parrent_folder)
            if temp_.folder_flag:
                logger.info(f'{i}.{j} - Каталог: {temp_.name} ' +
                            f'| Флаг каталога: {temp_.folder_flag} ' +
                            f'| Родительский каталог: {parrent_folder}')
            else:
                logger.info(f'{i}.{j} - Файл: {temp_.name} ' +
                            f'| Расширение: {temp_.extension} ' +
                            f'| Родительский каталог: {parrent_folder}')
            list_of_files.append(temp_)
    return list_of_files


if __name__ == "__main__":
    print(folder_content())