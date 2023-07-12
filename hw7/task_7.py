# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from os import listdir, path, mkdir, replace, getcwd
from pathlib import Path

__all__ = ['sort_files']

DICT_EXT = {"Музыка": ("mp3", "flac", "wav"),
            "Видео": ("mkv", "mp4", "avi"),
            "Изображения": ("jpg", "png", "gif"),
            "Текст": ("txt", "doc", "bin")}


def sort_files(directory):
    file_list = [files for files in listdir(directory)]
    for file in file_list:
        if path.isfile(directory+"/"+file):
            for fold, exts in DICT_EXT.items():
                if file.split(".")[-1] in exts:
                    dir_path = check_dir(directory, fold)
                    replace(directory + "/" + file, (dir_path + "/" + file))
    return file_list


def check_dir(dir_path, folder):
    name_fold = dir_path + folder
    if not folder in listdir(dir_path):
        mkdir(name_fold)
    return name_fold


if __name__ == "__main__":
    sort_files("./files/task_7/")