import copy


class Engine():
    def __init__(self, displacement=1000):
        self.displacement = displacement


class Wheel():
    def __init__(self, pressure=100):
        self.pressure = pressure


class Seat():
    def __init__(self, color=1):  # 1, 2, 3
        self.color = color


class Car():
    def __init__(self, engine, wheels, seats):
        self.engine = engine
        self.wheels = wheels
        # self.wheels= copy.deepcopy(wheels)
        self.seats = seats


if __name__ == '__main__':
    engine = Engine()
    wheels = [Wheel() for i in range(4)]
    seats = [Seat(color=3) for i in range(4)]

    car1 = Car(engine, wheels, seats)
    car2 = Car(engine, wheels, seats)

    print('\nENGINE', end='')
    print(car1.engine)
    print('\nSEATS', end='')
    print(car1.seats)
    print('\nWHEELS', end='')
    print(car1.wheels)

    print('\nWHEEL - PRESSURE')
    print('car 1:', car1.wheels[0].pressure)
    print('car 2:   ', car2.wheels[0].pressure)

    car1.wheels[0].pressure = 5

    print('\nWHEEL - PRESSURE after that we change the pressure of WHEEL 0 - CAR 1')
    # IF WE DON'T USE DEEPCOPY, CARS SHARE THE SAME 'WHEEL' OBJECT!
    print('car 1:', car1.wheels[0].pressure)
    print('car 2:', car2.wheels[0].pressure)
