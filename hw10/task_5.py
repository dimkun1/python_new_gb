# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish:
    """Для параметра length введите длину в см
    Для параметра water_solt введите 0, если рыба морская,
    любое другое значение - если рыба пресноводная"""

    def __init__(self, name, weigth, length, water_solt) -> None:
        self.name = name
        self.weigth = weigth
        self.length = length
        self.water_salt = water_solt

    def _get_length_info(self):
        if 0 < self.length < 10:
            group = "Мелкая"
        elif 10 <= self.length < 50:
            group = "Средняя"
        elif 50 <= self.length < 100:
            group = "Крупная"
        else:
            group = "Гигантская"
        return group

    def _get_water_salt_info(self):
        if self.water_salt == 0:
            return "морской"
        return "пресноводной"

    def get_specific(self):
        return f"Рыба {self.name} длиной {self.length} см относится к группе \
{self._get_length_info()} и является {self._get_water_salt_info()}"


class Bird:
    """Параметр course_season определяет, перелетная птица или нет.
    Параметр water_swim определяет, водоплавающая птица или нет.
    Введите введите 0, если параметр не является истинным"""

    def __init__(self, name, weigth, course_season, water_swim) -> None:
        self.name = name
        self.weigth = weigth
        self.course_season = course_season
        self.water_swim = water_swim

    def get_specific(self):
        if self.course_season == 0:
            course = "оседлым"
        else:
            course = "перелетным"
        if self.water_swim == 0:
            water = "не "
        else:
            water = ""
        return f"Птица {self.name} относится к {course} и {water}является перелетной"


class Mammal:
    """Для определения семейства (праметр family) введите следующие значения:
    1:Кошачьи, 2:Собачьи, 3:Медвежьи, 4:Гиеновые, 5:Куньи,
    6:Енотовые, 7:Тюленьи, 8:Магнустовые, 9:Моржовые, 10:Прочие.
    Параметр predator определяет, является ли животное хищником.
    Введите 0, если животное не является хищником"""

    def __init__(self, name, weigth, family, predator) -> None:
        self.name = name
        self.weigth = weigth
        self.family = family
        self.predator = predator

    def get_specific(self):
        family_dict = {1: "Кошачьих", 2: "Собачьих", 3: "Медвежьих", 4: "Гиеновых", 5: "Куньих",
                       6: "Енотовых", 7: "Тюленьих", 8: "Магнустовых", 9: "Моржовых", 10: "прочих"}
        if self.predator != 0:
            pred = "хищником"
        else:
            pred = "травоядным"
        return f"Животное {self.name} относится к семейству {family_dict[self.family]} и является {pred}"


if __name__ == "__main__":
    fish_ = Fish("Карась", "500", 30, 1)
    print(fish_.get_specific())

    bird_ = Bird("Сокол", "3000", 0, 0)
    print(bird_.get_specific())

    cat_ = Mammal("Лев", "50 кг", 1, 1)
    print(cat_.get_specific())

    help(Mammal)