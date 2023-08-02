# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

def request_int():
    while True:
        num = input('Введите число: ')
        try:
            result = float(num)
        except ValueError as e:
            print("Ведено не число. Попробуйте снова.")
        else:
            return int(result) if result%1 == 0 else result

if __name__ == "__main__":
    print(request_int())