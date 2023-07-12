# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными верными вариантами отгадок и количество попыток на угадывание.
# Функция возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['riddle']

def riddle(text, list_of_key, quntity_try):
    print(text)
    count = 1
    while quntity_try > 0:
        answer = input(f"У Вас {quntity_try} попыток. Введите Ваш ответ: ")
        if answer in list_of_key:
            print(f"Вы угадали с {count} попытки!")
            return count
        else:
            print(f"Неверно! Попробуйте ще раз!")
        count += 1
    return 0

if __name__ == "__main__":
    text = "Зимой и летом одним цветом"
    list_of_key = ["Ёлка", "елка", "ёлка", "Елка", "ель", "Ель"]
    quantity_try = 5

    riddle(text, list_of_key, quantity_try)