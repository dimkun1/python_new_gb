import json
from User import User
import Excep as ex


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
                users.append(User(name, int(uid), int(level)))
        return Project(users)

    def __str__(self):
        return "\n".join(str(k) for k in self.users)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.write_to_json("./result.json")

    def __del__(self):
        print("\tСессия завершена!")

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

    def write_to_json(self, path_file):
        with open(path_file, 'w', encoding='utf-8') as f:
            temp_dict = {k: "" for k in range(1, 8)}
            for user in self.users:
                for key, value in temp_dict.items():
                    if int(user.level) == key and value != "":
                        value.setdefault(str(user.uid), user.name)
                    elif int(user.level) == key and value == "":
                        temp_dict[key] = {str(user.uid): user.name}
            json.dump(temp_dict, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    u = Project.load_users("./users.json")
    with u:
        print(u)
        print(u.admin)
        print("___________________")
        u.enter('Sam',114)
        print(u.admin)
        print("___________________")
        u.add_user('Carl', 1014, 6)
        u.add_user('Crowly', 0, 5)
        print(u)
        print("___________________")
        u.del_user('Crowly', 0)
        print(u)
        u.add_user('Kas', 0, 5)