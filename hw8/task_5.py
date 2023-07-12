# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import pickle
import os


__all__ = ['json_to_pickle']


def json_to_pickle(directory):
    json_files = [file for file in os.listdir(
        directory) if file.endswith(".json")]
    for file_path in json_files:
        with (
            open(directory+file_path, "r", encoding="utf-8") as f,
            open(directory+file_path.replace(".json", ".pickle"), 'wb') as pickle_f
        ):
            pickle.dump(json.load(f), pickle_f)


if __name__ == "__main__":
    json_to_pickle("./files/task_5/")
    with open("./files/task_5/json_file.pickle", 'rb') as f_0:
        print(pickle.load(f_0))