# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов, которые также являются свойствами экземпляра.
# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Класс архива, котрый хранит пару свойств - число и строку.
    Дополнительно хранит в себе данные из ранее созданныъ экземпляров"""

    couple_list = []

    def __new__(cls, number, text):
        instance = super().__new__(cls)
        instance.number = number
        instance.text = text
        instance.couple_list.append((number, text))
        instance.list_of_saves = tuple(instance.couple_list)
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
    print(shelf1.get_last_saves())
    print(shelf2)
    print(shelf1)
    print(f"{shelf2=}")