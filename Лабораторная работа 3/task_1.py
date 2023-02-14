class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Конструктор для объекта класса Book
        :name: Название книги
        :author: Имя автора книги

        Пример: book1 = Book("Евгений Онегин","Пушкин")
        """
        self._name = name
        self.name
        self._author = author
        self.author

    @property
    def name(self) -> str:
        """
        Свойство возвращает название книги.
        Пример: book1.name
        """
        if not isinstance(self._name, str):
            raise TypeError("Название книги должно быть типа str")
        if self._name == "":
            raise ValueError("У книги должно быть название")
        return self._name

    @property
    def author(self) -> str:
        """
        Свойство возвращает имя автора книги.
        Пример: book1.author
        """
        if not isinstance(self._author, str):
            raise TypeError("Имя автора должно быть типа str")
        if self._author == "":
            raise ValueError("У автора должно быть имя")
        return self._author

    def __str__(self):
        """
        Метод возвращает название книги и имя автора в понятной для пользователя форме.
        Пример: book1.__str__
        """
        return f"Книга {self.name!r}. Автор {self.author!r}"

    def __repr__(self):
        """
        Метод возвращает атрибуты класса Book в более читабельном виде.
        Пример: book1.__repr__
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    """Дочерний класс PaperBook от класса Book."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Конструктор для объекта PaperBook с дополнительным атрибутом pages.
        :name: Название бумажной книги
        :author: Имя автора бумажной книги
        :pages: Количество станиц в бумажной книге

        Пример: paperbook1 = PaperBook("Евгений Онегин","Пушкин", 200)
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """
        Свойство возвращает количество страниц в книге.
        Пример: paperbook1.pages
        """
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Свойство устанавливает количество страниц в бумажной книге.
        Пример: paperbook1.pages = 250
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        """
        Метод возвращает атрибуты класса PaperBook в более читабельном виде
        Пример: paperbook1.__repr__
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):

    """Дочерний класс AudioBook от класса Book."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Конструктор для объекта класса AudioBook с дополнительным атрибутом duration.
        :name: Название аудиокниги
        :author: Имя автора аудиокниги
        :duration: Продолжительность аудиокниги

        Пример: audiobook1 = AudioBook("Евгений Онегин","Пушкин", 120.00)
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """
        Свойство возвращает продолжительность книги по времени прослушивания.
        Пример: audiobook1.duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """
        Свойство устанавливает продолжительность книги по времени прослушивания.
        Пример: audiobook1.duration = 200.00
        """
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги по времени прослушивания должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги по времени прослушивания должна быть положительным числом")
        self._duration = duration

    def __repr__(self):
        """
        Метод возвращает класса AudioBook в более читабельном виде
        Пример: audiobook1.__repr__
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    paper_book1 = PaperBook("Пикник на обочине", "Аркадий и Борис Стругацкие", 250)
    print(paper_book1.__str__())
    print(paper_book1.__repr__())

    audio_book1 = AudioBook("Евгений Онегин", "А.С. Пушкин", 120.50)
    print(audio_book1.__str__())
    print(audio_book1.__repr__())
