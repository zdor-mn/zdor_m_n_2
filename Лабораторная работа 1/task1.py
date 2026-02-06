# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Stol:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол"
        :param length: Длина стола
        :param width: Ширина стола
        :param height: Высота стола
        Примеры
        >>> stol = Stol(1200, 600, 750)
        """
        if not isinstance(length, (int,float)):
            raise TypeError("Длина стола должна быть int или float")
        if length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        self.length = length
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть int или float")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        self.width = width
        if not isinstance(height,(int, float)):
            raise TypeError("Высота стола должна быть int или float")
        if height <= 0:
            raise ValueError("Высота стола дожна быть положительным числом")
        self.height = height

    def surface(self) -> float:
        """
        Вычисляет площадь столешницы
        :return: Площадь столешницы
        Примеры:
        >>> stol = Stol(1200, 600, 750)
        >>> stol.surface()
        """
        ...
    def seats(self, seats: int) -> None:
        """
        Вычисляет количество мест
        :return: Количество мест
        Примеры:
        >>> stol = Stol(1200, 600, 750)
        >>> stol.seats(6)
        """
        if not isinstance(seats, int):
            raise TypeError("Количество мест должно быть int")
        if seats <= 0:
            raise ValueError("Количество мест должно быть положительным")
        ...


class Backpack:
    def init(self, capacity: float, color: str):
        """
        Создание и подготовка к работе объекта рюкзак.

        :param capacity: Объем рюкзака в литрах
        :param color: Цвет рюкзака

        Примеры:
        >>> backpack = Backpack(20, "blue")
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем должен быть int или float")
        if capacity <= 0:
            raise ValueError("Объем должен быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")

        self.capacity = capacity
        self.color = color

    def pack_item(self, volume: float) -> None:
        """
        Положить предмет в рюкзак.

        :param volume: Объем предмета
        :raise ValueError: Если предмет не помещается

        Примеры:
        >>> backpack = Backpack(20, "blue")
        >>> backpack.pack_item(5)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем предмета должен быть int float или")
        if volume < 0:
            raise ValueError("Объем не может быть отрицательным числом")
        ...

    def is_full(self) -> bool:
        """
        Проверка, полон ли рюкзак.
        :return: True если рюкзак заполнен полностью
        Примеры:
        >>> backpack = Backpack(20, "blue")
        >>> backpack.is_full()
        """

class Lamp:
    def init(self, brightness: float, color: str):
        """
        Создание и подготовка к работе объекта лампа.

        :param brightness: Яркость лампы в люменах
        :param color: Цвет лампы

        Примеры:
        >>> lamp = Lamp(800, "white")
        """
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость должна быть int или float")
        if brightness <= 0:
            raise ValueError("Яркость должна быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")

        self.brightness = brightness
        self.color = color

    def turn_on(self) -> None:
        """
        Включение лампы
        примеры:
        >>> lamp = Lamp(800, "white")
        >>> lamp.turn_on()
        """
        ...

    def chamge_brightness(self, brightness: float) -> None:
        """
        Регулировка яркости лампы.

        :param brightness: Новая яркость в люменах
        :raise ValueError: Если яркость отрицательная или нулевая
        Примеры:
        >>> lamp = Lamp(800, "white")
        >>> lamp.chamge_brightness(500)
        """
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость должна быть int или float")
        if brightness <= 0:
            raise ValueError("Яркость должна быть положительным числом")
        ...

if __name__ == "__task1__":
    doctest.testmod()
    pass


