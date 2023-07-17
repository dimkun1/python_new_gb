# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


__all__ = ['txt_to_json']


def txt_to_json (txt_file, json_file):
    output_dict = {}
    with(
    open(txt_file, 'r', encoding='utf-8') as f, \
    open(json_file, 'w', encoding='utf-8') as j_f
    ):
        while res := f.readline():
            output_dict[res.split()[0].capitalize()] = res.split()[1]
        json.dump(output_dict, j_f, indent=1)


if __name__ == "__main__":
    txt_to_json("C:\\G\\Project\\python_new_gb\\hw7\\files\\task_3\\total_file", "C:\\G\\Project\\python_new_gb\\hw8\\files\\task_1\\json_file.json")