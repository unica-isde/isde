from car_composition import Engine, Wheel, Seat
from typing import List


class Car:

    def __init__(
            self,
            engine: Engine,
            wheels: List[Wheel],
            seats: List[Seat]
    ) -> None:
        self.engine = engine
        self.seats = seats
        self.wheels = wheels
        self._n_wheels = None

    @property
    def n_wheels(
            self
    ) -> int:
        # LAZY INITIALIZATION
        if self._n_wheels is None:
            self._n_wheels = len(self.wheels)
        return self._n_wheels


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
