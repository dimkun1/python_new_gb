# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def get_value(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError:
        return default_value


if __name__ == "__main__":
    new_dict = {1: "one", 2: "two", 3: "three"}
    print(get_value(new_dict, 2, -1))