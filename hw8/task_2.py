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


def add_users(json_file):
    temp_dict = {}
    if path.isfile(json_file) and path.getsize(json_file) > 0:
        with open(json_file, 'r', encoding='utf-8') as f:
            temp_dict = json.load(f)
    while True:
        add_user = True
        while True:
            user_data = input("Введите через пробел имя пользователя, \
личный id и уровень доступа.\nДля выхода нажмите 0: ")
            if user_data == "0":
                sys.exit()
            user_name, user_id, level_access, *_ = user_data.split()
            if len(user_data.split()) != 3:
                print('Неверный формат ввода!')
            elif not int(level_access) in range (1,8):
                print('Уровень доступа должен быть в пределах от 1 до 7!')
            else:
                break
        for level, users in temp_dict.items():
            for uid in users:
                if uid == user_id:
                    print(f'Идентификатор {uid} уже существует в базе данных!')
                    add_user = False
                    break
            if add_user == False:
                break
        if add_user:
            for level, users in temp_dict.items():
                if level_access == level:
                    users.setdefault(user_id, user_name)
            temp_dict.setdefault(level_access, {user_id : user_name})
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(temp_dict, f, indent=2, sort_keys=True)


# def add_users(json_f):
#     if path.isfile(json_f):
#         with open (json_f, 'r', encoding='utf-8') as f:
#             dct = json.load(f)
#     else:
#         dct = {str(i):{} for i in range(1,8)}

#     while True:
#         data = input('Ввод: ')
#         if not data:
#             break
#         name, uid, access = data.split()
#         if uid in dct[access] and dct[access][uid] == name:
#             dct.setdefault(access, {uid:name})[uid] = name
#         print(dct)


if __name__ == "__main__":
    add_users("./files/task_2/json_file.json")
    # add_users("C:\\G\\Project\\python_new_gb\\hw8\\files\\task_2")