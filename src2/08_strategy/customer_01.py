class Customer:

    def __init__(self) -> None:
        self._cost: float = 0

    def print_bill(self) -> None:
        print(self._cost)

    def add_drink(
            self,
            n: int,
            unit_cost: float,
            happy_hour: bool = False
    ):
        cost = n * unit_cost
        if happy_hour:
            cost /= 2
        self._cost += cost

    @staticmethod
    def get_actual_dress(happy_hour: bool = False):
        if happy_hour:
            print("happy hour dress")
        else:
            print("normal dress")


if __name__ == "__main__":
    # NORMAL BILLING
    customer1 = Customer()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)
    customer1.add_drink(2, 5, happy_hour=True)
    customer1.get_actual_dress(happy_hour=True)

    # FINAL BILL
    customer1.get_actual_dress(happy_hour=True)
    customer1.print_bill()  # 12
