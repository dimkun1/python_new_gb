# Создайте класс МояСтрока где будут доступны все возможности str
# и дополнительно хранится имя автора строки и время создания (time.time)
# Добавьте к задачам 1 и 2 строки документации для классов.


import time


class MyString(str):
    """Наследованный класс строки.
    Дополнительно хранит в себе имя и время создания"""


    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creation_time = time.asctime()
        return instance


if __name__ == '__main__':
    author = 'Student'
    writing = 'Однажды в студёную зимнюю пору...'
    str_1 = MyString(writing, author)
    print(f'{str_1 = }')
    print(f'{str_1.author = }')
    print(f'{str_1.creation_time = }')
    help(MyString)