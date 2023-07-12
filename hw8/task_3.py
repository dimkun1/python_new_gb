# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


__all__ = ['json_to_csv']


def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as j_f:
        temp_dict = json.load(j_f)
    with open(csv_file, 'w', newline='', encoding='utf-8') as c_f:
        csv_write = csv.writer(c_f, dialect='excel')
        csv_write.writerow(["level", "id", "name"])
        all_data = []
        for level, users in temp_dict.items():
            for u_id, names in users.items():
                all_data.append([level, u_id, names])
        csv_write.writerows(all_data)


if __name__ == "__main__":
    json_to_csv("./files/task_2/json_file.json",
                "./files/task_3/csv_file.csv")