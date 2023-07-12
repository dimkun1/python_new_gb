# Задание №7 семинара 1.

N_MIN = 0
N_MAX = 999

while True:
    print('Введите число в диапазоне от', N_MIN, 'до', N_MAX, ':')
    num = int(input())
    if num >= N_MIN and num <= N_MAX:
        break
    print('Число вне диапазона!')

if num // 10 == 0:
    print('Введена цифра', num)
    res = num ** 2
    print('Квадрат числа', num, 'равен:')
elif num // 100 == 0:
    print('Введено двухзначное число', num)
    res = (num // 10) * (num % 10)
    print('произведение цифр числа', num, 'равно:')
else:
    print('Введено трехзначное число', num)
    res = num // 100 + num % 10 * 100 + num % 100 // 10 * 10
    print('зеркальное отображение числа', num, 'равно:')

print(res)