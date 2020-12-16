class Customer:
    def __init__(self, strategy):
        self.cost = 0
        self._strategy = strategy

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n, unit_cost):
        self.cost += self._strategy.get_actual_price(n * unit_cost)

    def set_strategy(self, strategy):
        self._strategy = strategy

    def get_actual_dress(self):
        self._strategy.get_actual_dress()

