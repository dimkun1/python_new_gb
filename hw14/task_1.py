# Создайте функцию, которая удаляет из текста
# все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import string


def del_symbols(input_text):
    unchecked_symbols = string.ascii_letters + ' '
    return "".join(char for char in input_text if char in unchecked_symbols).lower()

if __name__ == '__main__':
    text = "Hello, World!"
    print(del_symbols(text))