from customer import Customer
import strategy

# Prepare strategies

normal_strategy = strategy.NormalStrategy()
happy_hour_strategy = strategy.HappyHourStrategy()

# NORMAL BILLING

customer1 = Customer(normal_strategy)
customer1.add_drink(1, 7)

customer1.get_actual_dress()

# START HAPPY HOUR (50% discount)

customer1.set_strategy(happy_hour_strategy)
customer2 = Customer(happy_hour_strategy)

customer2.add_drink(1, 7)

customer1.add_drink(2, 5)
customer2.add_drink(2, 5)
customer1.get_actual_dress()

# FINAL BILL
customer1.get_actual_dress()

customer1.print_bill()  # 12
customer2.print_bill()  # 8.5
