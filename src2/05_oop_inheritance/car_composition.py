from typing import List


class Engine:

    def __init__(self, displacement=1000):
        self.displacement = displacement


class Wheel:

    def __init__(self, pressure=10):
        self.pressure = pressure


class Seat:

    def __init__(self, color=1):  # 1, 2, 3
        self.color = color


class Car:

    def __init__(
            self,
            engine: Engine,
            wheels: List[Wheel],
            seats: List[Seat]
    ) -> None:
        self.engine = engine
        self.wheels = wheels
        self.seats = seats
        self.n_wheels = len(self.wheels)

    def set_wheel_pressure(self, i_w, p):
        if i_w in range(0, self.n_wheels):
            self.wheels[i_w].pressure = p

    @property
    def displacement(self):
        return self.engine.displacement

    @property
    def wheels_pressure(self):
        return [w.pressure for w in self.wheels]

    @property
    def n_seats(self):
        return len(self.seats)


if __name__ == "__main__":

    import copy

    # Client
    engine = Engine(2000)  # displacement
    wheels = [Wheel(7)] * 4  # pressure 7, n wheels 4
    seats = [Seat(color=3)] * 5  # color 3,  n. seats 5
    car = Car(engine, wheels, seats)

    print("displacement:", car.displacement)
    print("wheel pressure:", car.wheels_pressure)  # [7, 7, 7, 7]

    car.set_wheel_pressure(0, 20)  # i in [0, 1, 2, 3]

    print("wheel pressure:", car.wheels_pressure)  # [1, 2, 3, 4]
    print("n seats:", car.n_seats)  # 5

    # create a second car
    # use deepcopy to avoid referencing the same wheels of the first car
    wheels2 = copy.deepcopy(wheels)
    car2 = Car(engine, wheels2, seats)
    car2.set_wheel_pressure(1, 100)

    print("car:", car.wheels_pressure)
    print("car2", car2.wheels_pressure)
