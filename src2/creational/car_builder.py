from abc import ABC, abstractmethod
from car import Car, Wheel, Engine, Body


class Director:
    # _builder = None

    def set_builder(self, builder):
        self._builder = builder

    def get_car(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        for _ in range(4):
            wheel = self._builder.get_wheel()
            car.attach_wheel(wheel)
        return car


class BuilderInterface(ABC):
    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass


class JeepBuilder(BuilderInterface):

    def get_body(self):
        body = Body('SUV')
        return body

    def get_engine(self):
        engine = Engine(400)
        return engine

    def get_wheel(self):
        wheel = Wheel(22)
        return wheel


class NissanBuilder(BuilderInterface):

    def get_body(self):
        body = Body('hatchback')
        return body

    def get_engine(self):
        engine = Engine(100)
        return engine

    def get_wheel(self):
        wheel = Wheel(16)
        return wheel


if __name__ == '__main__':
    d = Director()
    d.set_builder(JeepBuilder())
    jeep = d.get_car()
    print(jeep)

    d.set_builder(NissanBuilder())
    nissan = d.get_car()
    print(nissan)
