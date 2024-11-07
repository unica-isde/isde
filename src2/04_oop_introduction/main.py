from time_slot import TimeSlot


t1 = TimeSlot()
t1.set_h_m(2, 10)

print("total amount of minutes:", t1.get_m())
print("hours %d minutes %d" % t1.get_h_m())

t1.set_m(140)
print("total amount of minutes:", t1.get_m())
print("hours %d minutes %d" % t1.get_h_m())
