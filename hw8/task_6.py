# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv


__all__ = ['pickle_to_csv']


def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb',) as pickle_f:
        list_of_dict = [item for item in pickle.load(pickle_f).values()]
        headers = list(list_of_dict[0].keys())
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_f:
        csv_write = csv.DictWriter(csv_f, fieldnames=headers, dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(list_of_dict)


if __name__ == "__main__":
    pickle_to_csv("./files/task_6/json_file.pickle", \
                  "./files/task_6/csv_file.csv")