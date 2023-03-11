class A_Living_Thing():
    """Дочерний класс живое существо в комнате"""
    def __init__(self, kind: str, x_cor=1, y_cor=1):
        """
        Конструктор для объекта класса A_Living_Things с дополнительными атрибутами.
        Объект класса перенимает размер комнаты.
        :kind: тип живого существа
        :x_cor: местонахождение живого существа по координате x
        :y_cor: местонахождение живого существа по координате y
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
        self._y_cor = y_cor

    @property
    def coordinates(self) -> list:
        """
        Свойство геттер типа read-only для атрибута coordinates. Атрибут не должен быть изменен пользователем вручную.
        Возвращает значение атрибута coordinates.
        Пример: alive1.coordinates
        """
        return self._coordinates

    def move_around(self, new_x_cor=None, new_y_cor=None) -> None:
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

    def where_am_i(self) -> None:
        """"
        Выводит в консоль местоположение живого существа. Не принимает никаких аргументов
        Пример: alive1.where_am_i()
        output: [1, 1]
        """
        print(self.coordinates)

    def __str__(self) -> None:
        """
        Метод выводить в консоли тип объекта класса A_Living_Thing
        Пример: alive1.__str__()
        """
        print(f"Я живое существо типа '{self._kind.title()}'")

    def __repr__(self) -> str:
        """
        Метод __repr__, который возвращает атрибуты класса A_Living_Thing в более читабельном виде
        Пример: alive1.__repr__()
        """
        return f"{self.__class__.__name__}(kind={self.kind!r}, x_cor={self.x_cor!r}, " \
               f"y_cor={self.y_cor!r}, coordinates={self.coordinates!r}"


class Person(A_Living_Thing):
    """
    Дочерний класс "Человек"
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
            raise TypeError("Новое имя человека должно быть типа str")
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

    def where_am_i(self) -> None:
        """
        Метод выводит в консоль сообщение от человека о его местоположении. Не принимает никаких аргументов.
        Метод перезагружается, для соблюдения логики: человек может сказать свое местоположение.
        Пример: person1.where_am_i()
        output: I am at [1, 1]
        """
        print(f"I am at {self.coordinates}")

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


class Dog(A_Living_Thing):
    def __init__(self, kind: str, name: str, sex: str):
        """
                Конструктор для объекта "Собака"
                Атрибуты name и sex сделаны непубличными, чтобы пользователь не мог поменять их вручную.
                :name: имя собаки
                :sex: пол собаки

                Пример:
                person1 = Person("Собака", "Джин", "Кабель")
                """
        super().__init__(kind)
        self._name = name
        self.name
        self._sex = sex
        self.sex

    @property
    def name(self) -> str:
        """
        Свойство возвращает имя собаки
        Пример: self.name
        """
        if not isinstance(self._name, str):
            raise TypeError("Имя собаки должно быть типа str")
        if self._name == "":
            raise ValueError("У собаки должно быть имя")
        return self._name

    @property
    def sex(self):
        """
        Свойство геттер ипа read-only для атрибута sex.
        Пример: person1.sex
        """
        if not isinstance(self._sex, str):
            raise TypeError("Пол собаки должен быть типа str")
        if not self._sex.__eq__("Кабель") or self._sex.__eq__("Сучка"):
            raise ValueError("Собака может быть только Кабелём или Сучкой")
        return self._sex

    def where_am_i(self) -> None:
        """
        Метод выводит в консоли местоположение собаки, после того как она подаст голос. Метод не принимает аргументов.
        Метод перезагружается, для соблюдения логики: собака не может сказать свое местоположение, но его можно понять
        по ее лаю.
        Пример: dog1.where_am_i()
        output: Гав! Гав! Гав!
        [1, 1]
        """
        print("Гав! Гав! Гав!")
        print(self.coordinates)

if __name__ == "__main__":
    person1 = Person("Человек", "Tim", 21, "Мужской")
    person1.move_around(5, 6)
    person1.where_am_i()
    dog1 = Dog("Собака", "Джин", "Кабель")
    dog1.where_am_i()
    dog1.__str__()
