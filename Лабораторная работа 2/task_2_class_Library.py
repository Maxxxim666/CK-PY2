BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: ID книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError('id_ должно быть типа int')
        if id_ < 0:
            raise ValueError('id_ должно быть больше 0')
        self.id_ = id_
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages < 0:
            raise ValueError('Количество страниц должно быть больше 0')
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Создание и подготовка к работе объекта "Книга"
        :param books: Список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_: int) -> int:
        """
        Функция, которая возвращающает идентификатор для добавления новой книги в библиотеку
        :return: идентификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    @staticmethod
    def get_index_by_book_id(id_: int):
        """
        Функция, возвращающющая индекс книги в списке, который хранится в атрибуте экземпляра класса
        :return: индекс книги в списке, который хранится в атрибуте экземпляра класса
        """
        for identifier, books in enumerate(BOOKS_DATABASE):
            if 'id' in books and books['id'] == id_:
                return identifier
            else:
                return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(0))  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
