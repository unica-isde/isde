class Customer():
    def __init__(self, strategy):
        self.cost = 0
        self.get_price_strategy = strategy

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n, unit_cost):
        self.cost += self.get_price_strategy(n * unit_cost)
