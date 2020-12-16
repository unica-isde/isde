
from customer import Customer
from strategy import get_actual_price_normal
from strategy import get_actual_price_happy_hour

# NORMAL BILLING

customer1=Customer(get_actual_price_normal)
customer1.add_drink(1, 7)

# START HAPPY HOUR (50% discount)

customer1.get_price_strategy=get_actual_price_happy_hour
customer2=Customer(get_actual_price_happy_hour)

customer2.add_drink(1, 7)

customer1.add_drink(2, 5)
customer2.add_drink(2, 5)

# FINAL BILL

customer1.print_bill() # 12
customer2.print_bill() # 8.5




