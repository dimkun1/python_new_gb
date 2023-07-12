# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


_START_SIZE = 0


__all__ = ['folder_content_to_json', 'folder_content_to_csv', 'folder_content_to_pickle']


def _count_folder_size(folder):
    size = _START_SIZE
    for path_folder, _, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path_folder, f)
            size += os.path.getsize(fp)
    return size


def _content_in_folder(folder):
    dict_common = {}
    keys_of_dict = ['name', 'parrent_folder', 'type', 'size']
    for path_folder, folders, files in os.walk(folder):
        for i, item in enumerate(folders + files, start=1):
            name = item
            parrent_folder = path_folder
            abs_path = os.path.join(path_folder, item)
            if os.path.isfile(abs_path):
                type_ = "file"
                size = os.path.getsize(abs_path)
            elif os.path.isdir(abs_path):
                type_ = "folder"
                size = _count_folder_size(abs_path)
            dict_common.setdefault(path_folder, {})
            for path_, info in dict_common.items():
                if path_folder == path_:
                    info.setdefault(i, {key: value for key, value in
                                    zip(keys_of_dict, [name, parrent_folder, type_, size])})
    return dict_common


def folder_content_to_json(path_folder, path_file):
    with open(path_file, 'w', encoding='utf-8') as j_f:
        json.dump(_content_in_folder(path_folder), j_f, indent=2)


def folder_content_to_csv(path_folder, path_file):
    dict_to_read = _content_in_folder(path_folder)
    with open(path_file, 'w', newline="", encoding='utf-8') as c_f:
        csv_write = csv.DictWriter(
            c_f, fieldnames=['root_folder', 'name', 'parrent_folder', 'type', 'size'])
        csv_write.writeheader()
        all_data = []
        for content in dict_to_read.values():
            for mean in content.values():
                all_data.append(mean | {'root_folder': path_folder})
        csv_write.writerows(all_data)


def folder_content_to_pickle(path_folder, path_file):
    with open(path_file, 'wb') as p_f:
        pickle.dump(_content_in_folder(path_folder), p_f)


if __name__ == "__main__":
    input_dict = _content_in_folder(".\\files")
    folder_content_to_json(".\\files", '.\\files\\hw\\hw_json.json')
    folder_content_to_pickle(".\\files", '.\\files\\hw\\hw_pickle.pickle')
    folder_content_to_csv(".\\files", '.\\files\\hw\\hw_csv.csv')

    with open('.\\files\\hw\\hw_json.json', 'r', encoding='utf-8') as ff:
        diction_json = json.load(ff)
    print(diction_json)

    with open('.\\files\\hw\\hw_pickle.pickle', 'rb') as ff:
        diction_pickle = pickle.load(ff)
    print(diction_pickle)

