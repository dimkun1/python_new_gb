# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

__all__ = ['some_riddles']

QUATITY_TRY = 5

def riddle(text, list_of_key):
    print(text)
    for i in range (QUATITY_TRY):
        answer = input(f"У Вас {QUATITY_TRY} попыток. Введите Ваш ответ: ")
        if answer in list_of_key:
            print(f"Вы угадали с {i+1} попытки!")
            return i+1
        else:
            print(f"Неверно! Попробуйте еще раз!")
    return 0

def some_riddles():
    dict_riddle = {"Зимой и летом одним цветом":["Ёлка", "елка", "ёлка", "Елка", "ель", "Ель"],\
                   "Не расческа, а свистит":["Свисток", "Свист", "свисток"],
                   "Не ведро, а гавкает":["Собака", "пес", "Щенок"]}
    for rid, answ in dict_riddle.items():
        riddle(rid, answ)

if __name__ == "__main__":
    some_riddles()
