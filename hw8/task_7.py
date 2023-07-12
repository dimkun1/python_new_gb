# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


__all__ = ['csv_read_to_pickle']


def csv_read_to_pickle(csv_file):
    with open(csv_file, 'r', encoding='utf-8', newline="") as f:
        csv_read = csv.reader(f)
        headers = next(csv_read)
        list_for_pickle = []
        for line in csv_read:
            list_for_pickle.append(
                {key: value for key, value in zip(headers, line)})
        return pickle.dumps(list_for_pickle)


if __name__ == "__main__":
    pickle_string = csv_read_to_pickle("./files/task_6/csv_file.csv")
    print(pickle_string)
    print(pickle.loads(pickle_string))