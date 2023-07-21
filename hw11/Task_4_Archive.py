# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """Класс архива, котрый хранит пару свойств - число и строку.
    Дополнительно хранит в себе данные из ранее созданныъ экземпляров.
    Добавлены методы представления экземпляра для программтста и пользователя"""

    couple_list = []

    def __new__(cls, number, text):
        instance = super().__new__(cls)
        instance.number = number
        instance.text = text
        instance.list_of_saves = instance.couple_list + [(number, text)]
        instance.list_of_saves.remove((number, text))
        instance.couple_list.append((number, text))
        return instance

    def get_last_saves(self):
        return self.list_of_saves

    def __str__(self):
        return f"В объекте класса {Archive.__name__} хранятся цифры {self.number} " \
               f"и слова {self.text}. Предыдущие сохранения - {self.list_of_saves}"

    def __repr__(self):
        return f"{Archive.__name__}({self.number},{self.text})"


if __name__ == '__main__':
    shelf1 = Archive(1, "Колобок")
    print(shelf1)
    shelf2 = Archive(2, "Репка")
    shelf3 = Archive(3, "Курочка-ряба")
    print(shelf1.get_last_saves())
    print(shelf2)
    print(shelf1)
    print(f"{shelf2=}")
    print(f"{shelf1=}")
    print(f"{shelf3=}")
    print(shelf3)