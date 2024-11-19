from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def compute_price(self, value: float) -> float:
        pass  # DO NOTHING

    @abstractmethod
    def get_actual_dress(self) -> None:
        pass  # DO NOTHING


class NormalStrategy(Strategy):

    def compute_price(self, value: float) -> float:
        return value

    def get_actual_dress(self) -> None:
        print("normal dress")


class HappyHourStrategy(Strategy):

    def compute_price(self, value: float) -> float:
        discount = 0.5
        return value * discount

    def get_actual_dress(self) -> None:
        print("happy hour dress")


class Customer:

    def __init__(self, strategy: Strategy):
        self._cost: float = 0
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def print_bill(self) -> None:
        print(self._cost)

    def add_drink(self, n: int, unit_cost: float) -> None:
        self._cost += self.strategy.compute_price(n * unit_cost)

    def get_actual_dress(self) -> None:
        self.strategy.get_actual_dress()


if __name__ == "__main__":
    # Prepare strategies
    # strategies implement the methods
    # `compute_price` and `get_actual_dress`
    normal_strategy = NormalStrategy()
    happy_hour_strategy = HappyHourStrategy()

    # NORMAL BILLING
    customer1 = Customer(normal_strategy)
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)
    customer1.strategy = happy_hour_strategy
    customer2 = Customer(happy_hour_strategy)

    customer2.add_drink(1, 7)
    customer1.add_drink(2, 5)
    customer2.add_drink(2, 5)
    customer1.get_actual_dress()

    # FINAL BILL
    customer1.print_bill()  # 12
    customer2.print_bill()  # 8.5
