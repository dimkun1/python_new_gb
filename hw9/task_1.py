# Создайте функцию-замыкание, которая принимает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 


def guess_number(num, quantity_try):
    def game():
        print(f"Я загадаю случайное число.\nПопробуй его отгадать за {quantity_try} попыток")
        try_counter = quantity_try
        while try_counter > 0:
            input_data = int(input(f"Осталось {try_counter} попыток. Введите число: "))
            if input_data == num:
                print(f"Верно! Я загадал число {input_data}")
                break
            elif input_data > num:
                print("Меньше!")
            else:
                print("Больше!")
            try_counter -= 1
        else:
            print(f"Все попытки исчерпаны. Я загадал число {num}")

    return game


if __name__ == "__main__":
    number = 10
    quantity_try_ = 5
    result = guess_number(number, quantity_try_)
    result()