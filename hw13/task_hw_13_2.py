# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
from os import path
import sys


__all__ = ['add_users']


class BaseException(Exception):
    pass


class FileError(BaseException):
    def __init__(self, file_name) -> None:
        self.file_name = file_name.split("/")[-1]
        self.path = "/".join(path.abspath(file_name).split("\\")[:-1])

    def __str__(self) -> str:
        return f"Файла {self.file_name} в папке {self.path} не существует!"


class InputDataError(BaseException):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Количество вводимых через пробел значений должно быть равно 3! Вы ввели {len(self.value)} значения(й)!"


class UserNameError(BaseException):
    def __init__(self, value) -> None:
        self.value = value
        self.list_char = [k for k in value if not k.isalpha()]

    def __str__(self) -> str:
        return f"Введенное значение имени пользователя {self.value} содержит недопустимые символы: {self.list_char}!"


class LevelValueError(BaseException):
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Уровень доступа должен быть в пределах от 1 до 7! Вы ввели - '{self.value}'!"


class UserIDError(BaseException):
    def __init__(self, level, uid, user_name) -> None:
        self.level = level
        self.uid = uid
        self.user_name = user_name

    def __str__(self) -> str:
        return f"Пользователь с ID '{self.uid}' уже существует в базе! \
{self.uid}: {self.user_name} - уровень {self.level}"


def add_users(json_file):
    temp_dict = {}
    if not path.exists(json_file):
        raise FileError(json_file)
    with open(json_file, 'r', encoding='utf-8') as f:
        temp_dict = json.load(f)
    while True:
        user_data = input("Введите через пробел имя пользователя, \
личный id и уровень доступа.\nДля выхода введите 0: ")
        if user_data == "0":
            sys.exit()
        user_data_list = user_data.split()
        if len(user_data_list) != 3:
            raise InputDataError(user_data_list)
        user_name, user_id, level_access = user_data_list
        if not user_name.isalpha():
            raise UserNameError(user_name)
        if not level_access.isdigit() or not int(level_access) in range(1, 8):
            raise LevelValueError(level_access)
        for level, users in temp_dict.items():
            for uid in users:
                if uid == user_id:
                    raise UserIDError(level, uid, users[uid])
        for level, users in temp_dict.items():
            if level_access == level:
                users.setdefault(user_id, user_name)
        temp_dict.setdefault(level_access, {user_id: user_name})
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(temp_dict, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    add_users("./task_hw_13_2.json")