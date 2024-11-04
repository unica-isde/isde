minutes_in_hour = 60


def create_time_slot(h=0, m=0):
    tot_min = h * minutes_in_hour + m
    time_slot = {"minutes": tot_min}
    return time_slot


def set_time_slot_h_m(time_slot, h, m):
    tot_min = h * minutes_in_hour + m
    time_slot["minutes"] = tot_min


def set_m(time_slot, m):
    time_slot["minutes"] = m


def get_time_slot_h_m(time_slot):
    tot_min = time_slot["minutes"]
    hours = int(tot_min / minutes_in_hour)
    minutes = tot_min - hours * minutes_in_hour
    return hours, minutes


def get_time_slot_m(time_slot):
    return time_slot["minutes"]


# CLIENT
t1 = create_time_slot()

set_time_slot_h_m(t1, 2, 20)
print("total amount of minutes:", get_time_slot_m(t1))  # Expected value: 140
print("hours %d minutes %d" % get_time_slot_h_m(t1))  # Expected value: 2, 20

set_m(t1, 140)
print("total amount of minutes:", get_time_slot_m(t1))  # Expected value: 140
print("hours %d minutes %d" % get_time_slot_h_m(t1))  # Expected value: 2, 20
