# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint as rnd
from task_3 import Human


class Staff(Human):
    __COUNT_LEVEL = 7
    __MIN_ID_LIMIT = 100_000
    __MAX_ID_LIMIT = 999_999
    __list_id = []

    def __init__(self, *args):
        super().__init__(*args)
        while True:
            self.__uid = rnd(self.__MIN_ID_LIMIT, self.__MAX_ID_LIMIT)
            if self.__uid not in self.__list_id:
                self.__list_id.append(self.__uid)
                break
        self.__level = sum(j for j in map(int, (str(self.__uid)))) % self.__COUNT_LEVEL

    def get_uid(self):
        return self.__uid

    def get_level(self):
        return self.__level


if __name__ == "__main__":
    staf = Staff("Иванов", "Иван", "Иванович", 30, "муж.")
    print(staf.get_age())
    print(staf.get_sex())
    print(staf.full_name())
    staf.birthday()
    print(staf.full_name())
    print(staf.get_uid())
    print(staf.get_uid())
    print(staf._Staff__list_id)
    staf2 = Staff("ванов", "ван", "ванович", 3, "уж.")
    print(staf2.get_age())
    print(staf2.get_sex())
    print(staf2.full_name())
    staf2.birthday()
    print(staf2.full_name())
    print(staf2.get_uid())
    print(staf2.get_uid())
    print(staf2._Staff__list_id)
    print(staf2._Staff__list_id)