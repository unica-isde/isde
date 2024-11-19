from abc import ABC, abstractmethod
from typing import Type


class Customer(ABC):

    def __init__(self) -> None:
        self._cost: float = 0

    def print_bill(self) -> None:
        print(self._cost)

    @abstractmethod
    def add_drink(self, n: int, unit_cost: float) -> None:
        self._cost += n * unit_cost

    def change_class(self, new_class: Type["Customer"]) -> None:
        self.__class__ = new_class

    @staticmethod
    def get_actual_dress() -> None:
        print("normal dress")


class CustomerNormalHour(Customer):

    def add_drink(self, n: int, unit_cost: float) -> None:
        super().add_drink(n, unit_cost)


class CustomerHappyHour(Customer):

    def add_drink(self, n: int, unit_cost: float) -> None:
        discount = 0.5
        d_price = unit_cost * discount
        super().add_drink(n, d_price)

    @staticmethod
    def get_actual_dress() -> None:
        print("happy hour dress")


if __name__ == "__main__":
    # NORMAL BILLING
    customer1 = CustomerNormalHour()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)
    customer1.change_class(CustomerHappyHour)
    # You are changing class at runtime!
    # It is technically possible, but are we sure it is a good idea?

    customer1.add_drink(2, 5)
    customer1.get_actual_dress()

    # FINAL BILL
    customer1.get_actual_dress()
    customer1.print_bill()  # 12
