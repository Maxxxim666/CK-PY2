import doctest


class Person:
    def __init__(self, person_name: str, person_full_age: int):
        """
        Создание и подготовка к работе объекта "Человек"
        :param person_name: Имя человека
        :param person_full_age: Полный возраст человека
        Пример:
        >>> person_1 = Person("Maxim", 20)
        """
        if not isinstance(person_name, str):
            raise TypeError("Имя человека должно состоять из букв")
        if not person_name:
            raise ValueError("Строка пустая")
        self.person_name = person_name

        if not isinstance(person_full_age, int):
            raise TypeError("Возраст должен быть целым числом")
        if person_full_age < 0:
            raise ValueError("Возраст человека должен быть больше 0")
        self.person_full_age = person_full_age

    def change_name(self, new_person_name: str) -> None:
        """
        Функция, которая меняет имя человека
        :param new_person_name: Новое имя человека
        :raise TypeError: Если имя состоит не из букв, то вызываем ошибку
        :raise ValueError: Если имени нет, то вызываем ошибку
        Примеры:
        >>> person_1 = Person("Maxim", 20)
        >>> person_1.change_name("Andrey")
        """
        ...
        if not isinstance(new_person_name, str):
            raise TypeError("Имя человека должно состоять из букв")
        if not new_person_name:
            raise ValueError("Строка пустая")
        ...

    def change_full_age(self, new_full_age: int) -> None:
        """
        Функция, которая меняет полный возраст человека
        :param new_full_age: Новый полный возраст человека
        :raise ValueError: Если возраст меньше 0, то вызываем ошибку
        :raise TypeError: Если возраст не целое число, то вызываем ошибку
        Примеры:
        >>> person_1 = Person("Maxim", 20)
        >>> person_1.change_full_age(21)
        """
        ...
        if not isinstance(new_full_age, int):
            raise TypeError("Возраст должен быть целым числом")
        if new_full_age < 0:
            raise ValueError("Новый возраст должен быть больше 0")
        ...


class Window:
    def __init__(self, is_opened: bool, is_clean: bool):
        """
        Создание и подготовка к работе объекта "Окно"
        :param is_opened: Окно открыто (True), окно закрыто (False)
        :param is_clean: Окно чистое (True), окно грязное (False)
        Пример:
        >>> window_1 = Window(True, True)
        """
        if not isinstance(is_opened, bool):
            raise TypeError("Состояние окна должно быть типа bool")
        self.is_opened = is_opened

        if not isinstance(is_clean, bool):
            raise TypeError("Состояние окна должно быть типа bool")
        self.is_clean = is_clean

    def open_window(self) -> None:
        """
        Функция, которая открывает окно
        :raise ValueError: Если окно уже открыто, то вызываем ошибку
        Пример:
        >>> window_1 = Window(False, False)
        >>> window_1.open_window()
        """
        ...
        if self.is_opened:
            raise ValueError('Окно уже открыто!')
        ...

    def clean_window(self) -> None:
        """
        Функция, которая моет окно
        Пример:
        >>> window_1 = Window(True, False)
        >>> window_1.clean_window()
        """
        ...


class Car:
    def __init__(self, oil_amount: (int, float), oil_consumption: (int, float)):
        """
        Создание и подготовка к работе объекта "Машина"
        :param oil_amount: текущее количество топлива в баке
        :param oil_consumption: потребление топлива
        Пример:
        >>> car = Car(100, 10)
        """
        if not isinstance(oil_amount, (int, float)):
            raise TypeError('Количество топлива должно быть типа int или float')
        if oil_amount <= 0:
            raise ValueError('Количество топлива должно быть не меньше 0')
        self.oil_amount = oil_amount

        if not isinstance(oil_consumption, (int, float)):
            raise TypeError('Потребление топлива должно быть типа int или float')
        if oil_consumption < 0:
            raise ValueError('Потребление топлива должно быть больше 0')
        self.oil_consumption = oil_consumption

    def add_oil(self, extra_oil: (int, float)) -> None:
        """
        Функция, которая добавляет топлива в бак
        :param extra_oil: дополнительное топливо
        :raise ValueError: Если добавленное топливо меньше 0, то вызываем ошибку
        :raise TypeError: Если добавленное топливо не числового типа, то вызываем ошибку
        Пример:
        >>> car = Car(100, 10)
        >>> car.add_oil(10)
        """
        ...
        if not isinstance(extra_oil, (int, float)):
            raise TypeError('Добавленное топливо должно быть типа int или float')
        if extra_oil < 0:
            raise ValueError('Добавленное топливо должно быть больше 0')
        ...

    def get_current_oil_level(self) -> (int, float):
        """
        Функция, которая узнает текущий объем топлива
        :return: текущий объем топлива
        Пример:
        >>> car = Car(100, 10)
        >>> car.get_current_oil_level()
        100
        """
        return self.oil_amount


if __name__ == "__main__":
    doctest.testmod()
