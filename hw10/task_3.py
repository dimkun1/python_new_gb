# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.


class Human:

    def __init__(self, surname, name, patronymic, age, sex) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age
        self.__sex = sex

    def get_age(self):
        return self.__age

    def get_sex(self):
        return self.__sex

    def birthday(self):
        self.__age += 1
        return self.__age

    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic} - {self.__age} лет"


if __name__ == "__main__":
    human_1 = Human("Иванов", "Иван", "Иванович", 30, "муж.")
    print(human_1.get_age())
    print(human_1.get_sex())
    print(human_1.full_name())
    human_1.birthday()
    print(human_1.full_name())   