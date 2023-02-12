class Room:
    """Базовый класс Комната"""

    def __init__(self):
        """
        Конструктор для объекта Room создает комнату 10х10 кв.м.
        :x_line: длина стен комнаты по иксу
        :y_line: длина стен комнаты по игрику

        Пример: room1 = Room()
        """
        self._x_line = [x for x in range(0, 11)]
        self._y_line = [y for y in range(0, 11)]

    @property
    def x_line(self) -> list:
        """
        Геттер типа read-only для атрибута x_line
        Пример: self.x_line
        """
        return self._x_line

    @property
    def y_line(self) -> list:
        """
        Геттер типа read-only для атрибута y_line
        Пример: self.y_line
        """
        return self._y_line

    def __str__(self):
        """
        Магический метод __str__, который выводит в консоли размер комнаты в понятной для пользователя форме
        Пример: room1.__str__()
        """
        print(f"Размер комнаты: {self.x_line[-1]}x{self.y_line[-1]} кв.м.")

    def __repr__(self) -> str:
        """
        Магический метод __repr__, который возвращает атрибуты класса Room в более читабельном виде
        Пример: room1.__repr__()
        """
        return f"{self.__class__.__name__}(x_line={self.x_line!r}, y_line={self.x_line}"

class A_Living_Thing(Room):
    """Дочерний класс живое существо в комнате"""
    def __init__(self, kind: str, x_cor=1, y_cor=1):
        """
        Конструктор для объекта класса A_Living_Things с дополнительными атрибутами.
        Объект класса перенимает размер комнаты.
        :kind: тип живого существа
        :x_cor: местонахождение живого существа в комнате по координате икс
        :y_cor: местонахождение живого существа в комнате по координате игрик
        :coordinates: координаты местонахождение живого существа в комнате
        Пример: alive1 = A_Living_Thing("человек")
        """
        super().__init__()
        self._kind = kind
        self.kind
        self.x_cor = x_cor
        self.y_cor = y_cor
        self._coordinates = [x_cor, y_cor]
        self.coordinates

    @property
    def kind(self) -> str:
        """
        Свойство геттер типа read-only для атрибута kind. Атрибут не должен быть изменен пользователем вручную.
        Возвращает значение атрибута kind.
        Пример: alive1.kind
        """
        if not isinstance(self._kind, str):
            raise TypeError("Вид живого существа должен быть типа str")
        if self._kind == "":
            raise ValueError("У живого существа должно быть имя")
        return self._kind

    @property
    def x_cor(self) -> int:
        """
        Свойство возвращает значение атрибута x_cor
        Пример: alive1.x_cor
        """
        return self._x_cor

    @x_cor.setter
    def x_cor(self, x_cor) -> None:
        """
        Свойство проверяет и инициализирует значение для атрибута x_cor
        Пример: alive1.x_cor = 2
        """
        if not isinstance(x_cor, int):
            raise TypeError("Координаты должны быть типа int")
        if x_cor not in self.x_line[1:-1]:
            raise ValueError("Можно перемещаться по комнате только по координатам от 1 до 9 по x и y")
        self._x_cor = x_cor

    @property
    def y_cor(self) -> int:
        """
        Свойство возвращает значение атрибута y_cor
        Пример: alive1.y_cor
        """
        return self._y_cor

    @y_cor.setter
    def y_cor(self, y_cor) -> None:
        """
        Свойство проверяет и инициализирует значение для атрибута y_cor
        Пример: alive1.y_cor = 6
        """
        if not isinstance(y_cor, int):
            raise TypeError("Координаты должны быть типа int")
        if y_cor not in self.y_line[1:-1]:
            raise ValueError("Можно перемещаться по комнате только по координатам от 1 до 9 по x и y")
        self._y_cor = y_cor

    @property
    def coordinates(self) -> list:
        """
        Свойство геттер типа read-only для атрибута coordinates. Атрибут не должен быть изменен пользователем вручную.
        Возвращает значение атрибута coordinates.
        Пример: alive1.coordinates
        """
        return self._coordinates

    def move_in_the_room(self, new_x_cor=None, new_y_cor=None) -> None:
        """
        Метод изменяет местонахождение живого существа в комнате.
        Пример: alive1.move_in_the_room(5, 4)
        """
        if new_x_cor is None:
            self._coordinates[0] = self.x_cor
        else:
            self.x_cor = new_x_cor
            self._coordinates[0] = self.x_cor
        if new_y_cor is None:
            self._coordinates[1] = self.y_cor
        else:
            self.y_cor = new_y_cor
            self._coordinates[1] = self.y_cor

    def __str__(self) -> None:
        """
        Метод выводить в консоли тип объекта класса A_Living_Thing
        Пример: alive1.__str__()
        """
        print(f"Я живое существо типа{self._kind.title()}")

    def __repr__(self) -> str:
        """
        Метод __repr__, который возвращает атрибуты класса A_Living_Thing в более читабельном виде
        Пример: alive1.__repr__()
        """
        return f"{self.__class__.__name__}(kind={self.kind!r}, x_cor={self.x_cor!r}, " \
               f"y_cor={self.y_cor!r}, coordinates={self.coordinates!r}"


class Person(A_Living_Thing):
    """
    Базовый класс "Человек"
    """

    def __init__(self, kind: str, name: str, age: int, sex: str):
        """
        Конструктор для объекта "Человек"
        Атрибуты name и sex сделаны непубличными, чтобы пользователь не мог поменять их вручную
        :name: имя человека
        :age: возраст человека
        :sex: пол человека

        Пример:
        person1 = Person("Человек", "Игорь", 28, "Мужской")
        """
        super().__init__(kind)
        self.name = name
        self._age = age
        self.age
        self._sex = sex
        self.sex

    @property
    def name(self) -> str:
        """
        Свойство возвращает имя человека
        Пример: self.name
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Свойство, который инициализирует имя человека
        :new name: новое имя человека

        Примеры:
        >> person1.change_name("Николай")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имея человека должно быть типа str")
        if new_name == "":
            raise ValueError("У человека должно быть имя")
        self._name = new_name

    @property
    def age(self):
        """
        Свойство геттер ипа read-only для атрибута age.
        Пример: person1.age
        """
        if not isinstance(self._age, int):
            raise TypeError("Возраст человека должен быть типа int")
        if self._age <= 0:
            raise ValueError("Возраст человека не может быть меньше нуля или равен нулю")
        return self._age

    @property
    def sex(self):
        """
        Свойство геттер ипа read-only для атрибута sex.
        Пример: person1.sex
        """
        if not isinstance(self._sex, str):
            raise TypeError("Пол человека должен быть типа str")
        if not self._sex.__eq__("Мужской") or self._sex.__eq__("Женский"):
            raise ValueError("Пол человека может быть только мужским или женским")
        return self._sex

    def __str__(self):
        """
        Метод выводить в консоли имя объекта класса Person
        Пример: >>person1.greet()
        """
        print(f"Hi, my name is {self.name}")

    def __repr__(self) -> str:
        """
        Метод __repr__, который возвращает атрибуты класса Person в более читабельном виде
        Пример: person1.__repr__()
        """
        return f"{self.__class__.__name__}(kind={self.kind!r}, name={self.name!r}, " \
               f"age={self.age!r}, sex={self.sex!r}"

    @staticmethod
    def speak(speach: str):
        """
        Метод, который выводит в консоль любое передаваемое сообщение объекта Person
        :speach: сообщение, которое будет выведенно в консоли
        Примеры:
        >> person1.speak("С Новым Годом!")
        """
        if not isinstance(speach, str):
            raise TypeError("Фраза человека должна быть типа str")
        if speach == "":
            raise ValueError("Фраза передаваемая аргументом не может быть пустой str")
        print(speach)


if __name__ == "__main__":
    room1 = Room()
    room1.__str__()
    print(room1.__repr__())
    person1 = Person("Человек", "Игорь", 18, "Мужской")
    print(person1.coordinates)
    person1.move_in_the_room(3, 9)
    print(person1.coordinates)