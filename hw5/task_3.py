# Задача № 3 домашнего задания 5. Генератор чисел Фибоначчи.

def fibonacci_generator():
    yield 0
    a = 1
    b = 1
    while True:
        yield b
        a, b = b, a+b


NUMBER_OF_NUMBERS = 20

gen = fibonacci_generator()

for i in range(NUMBER_OF_NUMBERS):
    print(next(gen), end=' ')