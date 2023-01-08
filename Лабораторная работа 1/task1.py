# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Person:
    """
    Класс "Человек"
    """
    def __init__(self, name: str, age: int, sex: str):
        """
        Конструктор для объекта "Человек"
        :name: имя человека
        :age: возраст человека
        :sex: пол человека

        Пример:
        person1 = Person("Игорь", 28, "Мужской")
        """
        if not isinstance(name, str):
            raise TypeError("Имя человека должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст человека не может быть меньше нуля или равен нулю")
        self.age = age

        if not isinstance(sex, str):
            raise TypeError("Пол человека должен быть типа str")
        if sex != "Мужской" or "Женский":
            raise ValueError
        self.sex = sex

    def greet(self):
        """
        Метод выводить в консоли имя объекта класса Person

        >>person1.greet()
        """
        print(f"Hi, my name is {self.name}")

    def change_name(self, new_name: str):
        """
        Метод который меняет имя человека

        :new name: новое имя человека

        Примеры:
        >> person1.change_name("Николай")
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имея человека должно быть типа str")
        self.name = new_name

    def speak(self, speach: str):
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

class Door:
    """
    Класс Дверь
    """

    def __init__(self):
        """
        Конструктор для объекта дверь.
        Состояние двери не предусмотренно

        Примеры:
        >> door1 = Door()
        """
        self.is_closed = None
        self.close_the_door()
        self.is_open = None
        self.open_the_door()

    def close_the_door(self):
        """
        Метод который закрывает дверь

        Примеры:
        >> door1.close_the_door()
        """
        self.is_closed = True
        self.is_open = False

    def open_the_door(self):
        """
        Метод, который открывает дверь

        Примеры:
        >> door1.open_the_door()
        """
        self.is_closed = False
        self.is_open = True

class Student:

    def __init__(self, name: str, age: int, school_name: str):
        """
        Конструктор для объекта "Студент"
        :name: имя студента
        :age: возраст студента
        :school_name: название университета, в котором обучается студент

        Примеры:
        >> student1 = Student("Борис", 18, "Политехнический университет")
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст студента должен быть типа int")
        if age <= 18:
            raise ValueError("Возраст студента не может быть меньше 18 или равен 18")
        self.age = age

        if not isinstance(school_name, str):
            raise TypeError("Название университета должно быть типа str")
        self.school_name = school_name

    def change_school(self, school_name: str):
        """
        Метод, который меняет название университета, в котором обучается студент

        Примеры:
        >> student1.change_school("Высшая экономическая школа")
        """
        self.school_name = school_name

    def show(self):
        """
        Метод, который выводит в консоль имя студента, вораст студента и название университета, в котором обучается студент"

        Примеры:
        >> student1.show()
        """
        print(self.name, self.age, 'School:', self.school_name)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
