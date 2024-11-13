class Engine:

    def __init__(self, displacement=1000):
        self.displacement = displacement


class EngineWithWheels(Engine):

    def __init__(self, diplacement=1000, n_wheels=4, pressure=100):
        super().__init__(diplacement)
        self.n_wheels = n_wheels
        self.wheels_pressure = [pressure] * n_wheels

    def set_wheel_pressure(self, i_w, p):
        if i_w in range(0, self.n_wheels):
            self.wheels_pressure[i_w] = p


class Car(EngineWithWheels):

    def __init__(self, displacement=1000, n_wheels=4, pressure=100, n_seats=5):
        super().__init__(displacement, n_wheels, pressure)
        self.n_seats = n_seats


if __name__ == "__main__":
    car = Car(2000, 4, 7)  # displacement, n_wheels, pressure, n_seats

    print("displacement:", car.displacement)
    print("wheel pressure:", car.wheels_pressure)  # [7, 7, 7, 7]

    car.set_wheel_pressure(0, 1)
    car.set_wheel_pressure(1, 2)
    car.set_wheel_pressure(2, 3)
    car.set_wheel_pressure(3, 4)
    car.set_wheel_pressure(4, 5)  # NO ACTION - wheels are 0,1,2,3

    print("wheel pressure:", car.wheels_pressure)  # [1, 2, 3, 4]
    print("n seats:", car.n_seats)
