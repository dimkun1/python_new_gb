# Задание №2. Проверка числа на простоту.

MIN_NUM = 2
MAX_NUM = 100000
i = MIN_NUM

while True:
	print('Введите число в диапазоне от', MIN_NUM, 'до', MAX_NUM, ': ')
	num = int(input())
	if num < MIN_NUM or num > MAX_NUM:
		print('Введеное число находится вне диапазона!')
	else:
		break

while i <= num:
	if num != i and num % i == 0:
		print('Ваше число составное')
		quit()
	else:
		i += 1
		continue

print('Ваше число простое')