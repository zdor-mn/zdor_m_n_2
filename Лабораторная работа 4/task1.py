if __name__ == "__main__":
    class Car:
        """
        Базовый класс, описывающий автомобиль.
        """

        def __init__(self, brand: str, max_speed: int, fuel: float) -> None:
            """
            Конструктор базового класса.

            Args:
                brand (str): Марка автомобиля.
                max_speed (int): Максимальная скорость.
                fuel (float): Количество топлива.
            """
            self.brand: str = brand
            self.max_speed: int = max_speed
            self._fuel: float = fuel  # непубличный атрибут, чтобы топливо изменялось только через методы

        def __str__(self) -> str:
            return f"Car brand: {self.brand}, max speed: {self.max_speed}"

        def __repr__(self) -> str:
            return f"Car(brand={self.brand!r}, max_speed={self.max_speed!r}, fuel={self._fuel!r})"

        def drive(self, distance: float) -> float:
            """
            Метод движения автомобиля.

            Args:
                distance (float): Пройденная дистанция.

            Returns:
                float: Оставшееся количество топлива.
            """
            consumption: float = distance * 0.1
            self._fuel -= consumption
            return self._fuel

        def transport(self, weight: float) -> str:
            """
            Метод перевозки груза.

            Args:
                weight (float): Вес груза.

            Returns:
                str: Сообщение о перевозке.
            """
            return f"Car transports cargo weighing {weight} kg."


    class PassengerCar(Car):
        """
        Дочерний класс, описывающий легковой автомобиль.
        """

        def __init__(self, brand: str, max_speed: int, fuel: float, seats: int) -> None:
            """
            Конструктор легкового автомобиля.

            Args:
                brand (str): Марка автомобиля.
                max_speed (int): Максимальная скорость.
                fuel (float): Количество топлива.
                seats (int): Количество пассажирских мест.
            """
            super().__init__(brand, max_speed, fuel)
            self.seats: int = seats

        def __str__(self) -> str:
            return f"Passenger car {self.brand}, seats: {self.seats}, max speed: {self.max_speed}"

        def transport(self, passengers: int) -> str:
            """
            Переопределённый метод перевозки.

            Причина переопределения:
            В легковом автомобиле перевозятся пассажиры,
            поэтому метод работает с количеством пассажиров,
            а не с весом груза.

            Args:
                passengers (int): Количество пассажиров.

            Returns:
                str: Сообщение о перевозке пассажиров.
            """
            if passengers > self.seats:
                return "Too many passengers!"
            return f"Passenger car transports {passengers} passengers."


    if __name__ == "__main__":

        car = Car("Toyota", 180, 50)
        print(car)
        print(car.drive(100))

        passenger_car = PassengerCar("Volkswagen", 190, 50, 5)
        print(passenger_car)
        print(passenger_car.transport(4))
    pass
