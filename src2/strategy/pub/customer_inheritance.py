class CustomerNormalHour:
    def __init__(self):
        self.cost = 0

    def print_bill(self):
        print(self.cost)

    def add_drink(self, n, unit_cost):
        self.cost += n * unit_cost

    @staticmethod
    def get_actual_dress():
        print('normal dress')


class CustomerHappyHour(CustomerNormalHour):

    def add_drink(self, n, unit_cost):
        discount = 0.5
        self.cost += discount * (n * unit_cost)

    @staticmethod
    def get_actual_dress():
        print('happy hour dress')


if __name__ == '__main__':
    # NORMAL BILLING
    customer1 = CustomerNormalHour()
    customer1.add_drink(1, 7)
    customer1.get_actual_dress()

    # START HAPPY HOUR (50% discount)
    customer1.__class__ = CustomerHappyHour
    # You are changing class at runtime.
    # It is possible, but are we sure it is a good idea?

    customer1.add_drink(2, 5)
    customer1.get_actual_dress()

    # FINAL BILL
    customer1.get_actual_dress()
    customer1.print_bill()  # 12
