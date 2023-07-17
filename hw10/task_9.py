# Возьмите любую из задач с прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса,
# а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Прочитайте csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json
import csv


class CsvToJson:

    def __init__(self, csv_file):
        self.csv_file = csv_file


    def format(self):
        json_file = self.csv_file.replace(".csv",".json")
        with(
            open(self.csv_file, 'r', newline='', encoding='utf-8') as c_f, \
            open(json_file, 'w', encoding='utf-8') as j_f
        ):
            dict_for_json = {}
            read_file = csv.reader(c_f)
            keys = next(read_file)
            for i, line in enumerate(read_file, start=1):
                dict_for_json[i] = {key : value for key, value in zip(keys, line)}
            for value in dict_for_json.values():
                for key, item in value.items():
                    if key == "id":
                        if len(item) < 10:
                            value[key] = "0"*(10-len(item))+item
                    if key == "name":
                        value[key] = item.capitalize()
                value["hash"] = value["id"] + value["name"]
            json.dump(dict_for_json, j_f, indent=2)

if __name__ == "__main__":
    ex = CsvToJson("./hw10/task_9.csv")
    ex.format()