# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв. Названия предметов должны загружаться
# из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5)+
# и результаты тестов (от 0 до 100).+
# Также экземпляр должен сообщать средний балл по тестам +
# для каждого предмета и по оценкам всех предметов вместе взятых. +

import csv
import json
from os import path
from random import randint as rnd

_DOWN_LIMIT_SUBJECT = 2
_UP_LIMIT_SUBJECT = 5
_DOWN_LIMIT_TEST = 0
_UP_LIMIT_TEST = 100
_SUBJECT = "предмет"
_TEST = "тест"
_LIST_DSCIPLINE = "list.csv"


class Descriptor:
    def __init__(self, down_limit_test: int = None, up_limit_test: int = None,
                 down_limit_subject: int = None, up_limit_subject: int = None,
                 list_disciplines=_LIST_DSCIPLINE):
        self.list_disciplines = list_disciplines
        self.down_limit_test = down_limit_test
        self.up_limit_test = up_limit_test
        self.down_limit_subject = down_limit_subject
        self.up_limit_subject = up_limit_subject

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.validate_name(value)
        if isinstance(value, dict):
            self.validate_dict(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate_name(self, value):
        if value.capitalize() != value or not value.isalpha():
            raise ValueError(f'Значение "{value}" должно начинаться с заглавной буквы и \
не должно содержать ничего, кроме букв')

    def _create_dict_subject(self):
        with open(self.list_disciplines, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            return {line[0]: line[1] for line in reader}

    def validate_dict(self, value):
        temp_dict = self._create_dict_subject()
        for subject, score in value.items():
            if isinstance(score, int) == False:
                raise ValueError(
                    f'Оценка или результат теста должны быть целым числом')
            if subject not in temp_dict:
                raise ValueError(
                    f'Значение "{subject}" отсутствует в списке предметов')
            if self.down_limit_test is not None and self.up_limit_test is not None \
                    and temp_dict[subject] == _TEST \
                    and score not in range(_DOWN_LIMIT_TEST, _UP_LIMIT_TEST+1):
                raise ValueError(
                    f'Результат теста "{subject}: {score}" должно быть в диапазоне {_DOWN_LIMIT_TEST, _UP_LIMIT_TEST}')
            if self.down_limit_subject is not None and self.up_limit_subject is not None \
                    and temp_dict[subject] == _SUBJECT \
                    and score not in range(_DOWN_LIMIT_SUBJECT, _UP_LIMIT_SUBJECT+1):
                raise ValueError(
                    f'Оценка по предмету "{subject}: {score}" должно быть в диапазоне {_DOWN_LIMIT_SUBJECT, _UP_LIMIT_SUBJECT}')


class Student:

    name = Descriptor()
    surname = Descriptor()
    patronymic = Descriptor()
    dict_discipline = Descriptor(
        _DOWN_LIMIT_TEST, _UP_LIMIT_TEST, _DOWN_LIMIT_SUBJECT, _UP_LIMIT_SUBJECT)

    def __init__(self, *args):
        self.dict_discipline = {}
        if len(args) == 3:
            self.surname, self.name, self.patronymic = args
        elif len(args) == 1:
            self.surname, self.name, self.patronymic = args[0].split()
        else:
            raise ValueError(
                "Необходимо ввести ФИО одной строкой или отдельными значениями")

    def _create_dict_subject(self, list_disciplines=_LIST_DSCIPLINE):
        with open(list_disciplines, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            return {line[0]: line[1] for line in reader}

    def generate_scores(self):
        with open(f"{self.surname}_{self.name[0]}_{self.patronymic[0]}.json", "w", encoding='utf-8') as f:
            temp_dict = {}
            for name_sub, kind in self._create_dict_subject(_LIST_DSCIPLINE).items():
                if kind == _SUBJECT:
                    temp_dict[name_sub] = rnd(
                        _DOWN_LIMIT_SUBJECT, _UP_LIMIT_SUBJECT)
                elif kind == _TEST:
                    temp_dict[name_sub] = rnd(
                        _DOWN_LIMIT_TEST, _UP_LIMIT_TEST)
            json.dump(temp_dict, f, indent=2, ensure_ascii=False)
        self.dict_discipline = temp_dict

    def put_score(self, subject, score):
        file_name = f"{self.surname}_{self.name[0]}_{self.patronymic[0]}.json"
        if path.isfile(file_name) and path.getsize(file_name) > 0:
            with open(file_name, "r", encoding='utf-8') as f:
                temp_dict = json.load(f)
        else:
            temp_dict = {}
        temp_dict[subject] = score
        self.dict_discipline = temp_dict
        with open(file_name, "w", encoding='utf-8') as f:
            json.dump(temp_dict, f, indent=2, ensure_ascii=False)

    def average_subject(self):
        sum = 0
        count = 0
        for name_sub, kind in self._create_dict_subject(_LIST_DSCIPLINE).items():
            if kind == _SUBJECT and name_sub in self.dict_discipline.keys():
                sum += self.dict_discipline[name_sub]
                count += 1
        return sum/count if count > 0 else 0

    def average_test(self):
        sum = 0
        count = 0
        for name_sub, kind in self._create_dict_subject(_LIST_DSCIPLINE).items():
            if kind == _TEST and name_sub in self.dict_discipline.keys():
                sum += self.dict_discipline[name_sub]
                count += 1
        return sum/count if count > 0 else 0

    def __str__(self):
        if self.dict_discipline:
            return f"{self.surname} {self.name[0]}.{self.patronymic[0]}.\n\t" +\
                "\n\t".join(f"{discipline}: {score}" for discipline, score in self.dict_discipline.items()) +\
                f"\nСредний бал по предметам: {self.average_subject()}\tСредний бал по тестам: {self.average_test()}"
        else:
            return f"{self.surname} {self.name[0]}.{self.patronymic[0]}.\n\t" +\
                "Оценки не выставлены"


if __name__ == "__main__":
    pii = Student("Петров", "Иван", "Иванович")
    ipa = Student("Иванов Петр Аркадьевич")
    print(ipa)
    # pro = Student("Птичкин Р8ман Олегович") #ValueError: Значение "Р8ман" должно начинаться с заглавной буквы и не должно содержать ничего, кроме букв
    # pro = Student("птичкин Роман Олегович") #ValueError: Значение "птичкин" должно начинаться с заглавной буквы и не должно содержать ничего, кроме букв
    print("----------")
    ipa.put_score("История", 10)
    print(ipa)
    # ipa.put_score("физра", 10) #ValueError: Значение "физра" отсутствует в списке предметов
    print("----------")
    print(ipa)
    ipa.generate_scores()
    print("----------")
    print(ipa)
    # ipa.put_score("Математика", 0) #ValueError: Оценка по предмету "Математика: 0" должно быть в диапазоне (2, 5)
    # print(ipa)
    print("----------")
    print("----------")
    print(pii)
    pii.generate_scores()
    print("----------")
    print(pii)