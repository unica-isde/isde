class Car:
    def __init__(self):
        self._wheels = list()
        self._engine = None
        self._body = None

    def set_body(self, body):
        self._body = body

    def attach_wheel(self, wheel):
        self._wheels.append(wheel)

    def set_engine(self, engine):
        self._engine = engine

    def __str__(self):
        return "CAR ->" + \
               "\nbody: %s" % self._body.shape + \
               "\nengine horsepower: %s" % self._engine.horsepower + \
               "\ntire size: %d" % self._wheels[0].size


# CAR parts

class Wheel:
    def __init__(self, size):
        self.size = size


class Engine:
    def __init__(self, hp):
        self.horsepower = hp


class Body:
    def __init__(self, shape):
        self.shape = shape
