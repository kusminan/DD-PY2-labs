class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает имя автора книги."""
        return self._author

    def __str__(self):
        """Возвращает название книги и имя автора в понятной для пользователя форме."""
        return f"Книга {self.name!r}. Автор {self.author!r}"

    def __repr__(self):
        """Возвращает атрибуты класса Book в более читабельном виде."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    """Дочерний класс PaperBook от класса Book."""

    def __init__(self, name: str, author: str, pages: int):
        """Конструктор PaperBook с дополнительным атрибутом pages."""
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        """Возвращает атрибуты класса PaperBook в более читабельном виде"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):

    """Дочерний класс AudioBook от класса Book."""

    def __init__(self, name: str, author: str, duration: float):
        """Конструктор AudioBook с дополнительным атрибутом duration."""
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги по времени прослушивания."""
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность книги по времени прослушивания."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги по времени прослушивания должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги по времени прослушивания должна быть положительным числом")
        self._duration = duration

    def __repr__(self):
        """Возвращает атрибуты класса AudioBook в более читабельном виде"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

if __name__ == "__main__":
    paper_book1 = PaperBook("Пикник на обочине", "Аркадий и Борис Стругацкие", 250)
    print(paper_book1.__str__())
    print(paper_book1.__repr__())

    audio_book1 = AudioBook("Евгений Онегин", "А.С. Пушкин", 120.50)
    print(audio_book1.__str__())
    print(audio_book1.__repr__())
