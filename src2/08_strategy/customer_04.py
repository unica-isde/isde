from typing import Callable


def dress_normal_strategy() -> None:
    print("normal dress")


def dress_happy_hour_strategy() -> None:
    print("happy hour dress")


def compute_price_normal_strategy(value: float) -> float:
    return value


def compute_price_happy_hour(value: float) -> float:
    discount = 0.5
    return value * discount


class Customer:

    def __init__(
            self,
            strategy_price: Callable,
            strategy_dress: Callable
    ):
        self._cost: float = 0
        self.compute_price = strategy_price
        self.get_actual_dress = strategy_dress

    def add_drink(self, n: int, unit_cost: float) -> None:
        self._cost += self.compute_price(n * unit_cost)

    def print_bill(self) -> None:
        print(self._cost)


if __name__ == "__main__":
    customer1 = Customer(compute_price_normal_strategy, dress_normal_strategy)
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()


    # START HAPPY HOUR (50% discount)
    customer1.compute_price = compute_price_happy_hour
    customer1.get_actual_dress = dress_happy_hour_strategy
    customer1.add_drink(2, 5)
    customer1.get_actual_dress()

    customer1.print_bill()  # 12
