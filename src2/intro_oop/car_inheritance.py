class Engine():
    def __init__(self, displacement=1000):
        self.displacement = displacement


class EngineWithWheels(Engine):
    def __init__(self, displacement=1000, nWheels=4, pressure=100):
        super().__init__(displacement)
        self.nWheels = nWheels
        self.wheels_pressure = pressure

class Car(EngineWithWheels):
    def __init__(self, displacement=1000, nWheels=4, pressure=100, nSeats=5):
        super().__init__(displacement, nWheels, pressure)
        self.nSeats = nSeats

if __name__ == '__main__':
    car = Car(2000, 5, 7)

    print('displacemeent:', car.displacement)
    print('wheel pressure:', car.wheels_pressure)
    print('n seats:', car.nSeats)
