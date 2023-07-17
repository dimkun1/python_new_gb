# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа. Внутри класса создайте экземпляр
# на основе переданного типа и верните его из класса-фабрики.

import task_6 as An


class AnimalsFactory:

    def create_animal(self, animal_type: str, *args) -> An.Animal | An.Fish | An.Bird | An.Mammal:
        new_animal = self._get_maker(animal_type)
        return new_animal(*args)

    def _get_maker(self, animal_type: str):
        types = {"fish": An.Fish, "bird": An.Bird, "mammal": An.Mammal, "animal": An.Animal}
        return types[animal_type.lower()]


if __name__ == "__main__":
    fabric = AnimalsFactory()
    ex_1 = fabric.create_animal("Fish", 30, 1, "Карась", 500)
    print(type(ex_1))
    print(ex_1.get_specific())

    ex_2 = fabric.create_animal("Animal", "Лев", 50)
    print(type(ex_2))
    print(ex_2.get_params())

# import Task_6_Animals as An

# class AnimalsFactory:

#     def __init__(self, animal_cls, *args):
#         self.animal_cls = animal_cls(*args)
#         self.args = args

#     def crate_class(self) -> An.Animal | An.Fish | An.Bird | An.Mammal:
#         return self.animal_cls

# if __name__ == "__main__":
#     ex_1 = AnimalsFactory(An.Fish, 30, 1, "Карась", 500)
#     print(type(ex_1))
#     animal_1 = ex_1.crate_class()
#     print(type(animal_1))
#     print(animal_1.get_specific())

#     ex_2 = AnimalsFactory(An.Animal, "Лев", 50)
#     print(type(ex_2))
#     animal_2 = ex_2.crate_class()
#     print(type(animal_2))
#     print(animal_2.get_params())