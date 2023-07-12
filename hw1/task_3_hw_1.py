# Задание №3. Угадывание числа.

from random import randint

LIMIT_MAX = 1000
LIMIT_MIN = 0
NUMBER_ATTEMPTS = 10

i = NUMBER_ATTEMPTS
num = randint(0, 1000)

print('Угадай число от', LIMIT_MIN, 'до', LIMIT_MAX, 'с', NUMBER_ATTEMPTS, 'попыток')

while i > LIMIT_MIN:
	print('Попытка', NUMBER_ATTEMPTS - i + 1)
	n = int(input('введите число: '))
	i -= 1
	if n == num:
		print('Ура! Угадал!')
		quit()
	else:
		print('Не угадал  :(')
		if num > n:
			print('Загаданное число больше введенного.')
		else:
			print('Загаданное число меньше введенного.')
		continue

print('Сожалею, но попытки закончились! Загаданное число', num)