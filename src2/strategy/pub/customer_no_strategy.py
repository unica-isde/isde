class CustomerNoStrategy:
    def __init__(self):
        self.cost = 0

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n, unit_cost, happy_hour=False):
        cost = n * unit_cost
        if happy_hour:
            cost = cost / 2
        self.cost += cost

    @staticmethod
    def get_actual_dress(happy_hour=False):
        if happy_hour:
            print('happy hour dress')
        else:
            print('normal dress')


if __name__ == '__main__':
    # NORMAL BILLING
    customer1 = CustomerNoStrategy()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)
    customer1.add_drink(2, 5, happy_hour=True)
    customer1.get_actual_dress(happy_hour=True)

    # FINAL BILL
    customer1.get_actual_dress(happy_hour=True)
    customer1.print_bill()  # 12
