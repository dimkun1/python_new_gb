# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k рассчитанных фаториалов.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов

import json


class Factorial:

    def __init__(self, k):
        self.k = k
        self.history_list = []

    def __call__(self, value):
        fact = 1
        for i in range(1, value+1):
            fact *= i
        self.history_list.append({value: fact})
        self.history_list = self.history_list[-self.k:]
        return fact

    def show_history(self):
        return self.history_list

    def __enter__(self):
        # pass
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("./les_12/" + self.__class__.__name__ + ".json", 'w', encoding='utf-8') as f:
            json.dump(self.history_list, f, indent=1)


if __name__ == "__main__":
    f = Factorial(8)
    with f:
        for i in range(2, 14):
            print(f(i))
    print(f.show_history())