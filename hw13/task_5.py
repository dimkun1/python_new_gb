# Доработайте задачи 3 и 4. Создайте класс Project, содержащий атрибуты -
# список пользователей проекта и админ проекта. Класс имеет следующие методы:
#  - Классовый метод загрузки данных из JSON-файла (из 2 задачи семинара 8)
#  - Метод входа в систему - требует указать имя и id пользователя. Далее
# метод создает пользователя и проверяет, есть ли он в списке пользователей
# проекта. Если пользователь присутствует в списке пользователей проекта,
# то пользователь, который входит получает его уровень доступа и становится
# администратором.
#  - Метод добавления пользователя в список пользователей. Если уровень
# пользователя меньше, чем уровень администратора, вызывайте исключение уровня
# доступа.
#  - * Метод удаления пользователя из списка пользователей проекта
#  - * Метод сохранения списка пользователей в JSON-файл при выходе
# из контекстного менеджера


import json
from task_4 import User
import task_3 as ex


class Project:

    def __init__(self, users) -> None:
        self.users = users
        self.admin = None

    @classmethod
    def load_users(cls, file):
        with open(file, 'r', encoding="utf-8") as f:
            temp = json.load(f)
        users = []
        for level, user in temp.items():
            for uid, name in user.items():
                users.append(User(name, uid, level))
        return Project(users)

    def __str__(self):
        return "\n".join(str(k) for k in self.users)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write_to_json()

    def __del__(self):
        print("Сессия завершена!")

    def enter(self, name, uid):
        new_user = User(name, uid)
        if not new_user in self.users:
            raise ex.ErrorAcsess(name, uid)
        for user in self.users:
            if new_user == user:
                new_user.level = user.level
                self.admin = new_user

    def add_user(self, name, uid, level):
        if int(self.admin.level) > level:
            raise ex.ErrorLevel(name, level, self.admin)
        else:
            new_user = User(name, uid, level)
            if new_user in self.users:
                raise ex.ErrorUser(name, uid)
            self.users.append(new_user)

    def del_user(self, name, uid):
        new_user = User(name, uid)
        if not new_user in self.users:
            raise ex.ErrorAcsess(name, uid)
        for user in self.users:
            if new_user == user:
                new_user.level = int(user.level)
        if int(self.admin.level) > new_user.level:
            raise ex.ErrorLevel(name, new_user.level, self.admin)
        else:
            self.users.remove(new_user)

    def write_to_json(self):
        with open("./result.json", 'w', encoding='utf-8') as f:
            temp_dict = {k: "" for k in range(1, 8)}
            for user in self.users:
                for key, value in temp_dict.items():
                    if int(user.level) == key and value != "":
                        value.setdefault(str(user.uid), user.name)
                    elif int(user.level) == key and value == "":
                        temp_dict[key] = {str(user.uid): user.name}
            json.dump(temp_dict, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    u = Project.load_users("./task_2.json")
    with u:
        print(u)
        print(u.admin)
        print("___________________")
        u.enter('Sam', '114')
        print(u.admin)
        print("___________________")
        u.add_user('Crowly', 0, 6)
        print(u)
        print("___________________")
        u.del_user('Crowly', 0)
        print(u)
        u.add_user('Kas', 0, 5)