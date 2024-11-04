minutes_in_hour = 60


def create_time_slot(h=0, m=0):
    """generates the data structure"""
    time_slot = {"h": h, "m": m}
    return time_slot


def get_m(time_slot):
    """returns a string representing the total amount of minutes"""
    return time_slot["h"] * minutes_in_hour + time_slot["m"]


def get_h_m(time_slot):
    """returns a tuple representing  (hours, minutes)"""
    return time_slot["h"], time_slot["m"]


def set_m(time_slot, m):
    """initializes the data structure with the total amount of minutes"""
    time_slot["h"] = int(m / minutes_in_hour)
    time_slot["m"] = m % minutes_in_hour


def set_h_m(time_slot, h, m):
    """initialize the data structure with (hours, minutes)"""
    time_slot["h"] = h
    time_slot["m"] = m


# CLIENT - an example

t1 = create_time_slot()
# You must create a time slot "object" before using set and get

set_h_m(t1, 2, 20)
print(get_m(t1))  # Expected value: 140
print(get_h_m(t1))  # Expected value: 2, 20

set_m(t1, 140)
print(get_m(t1))  # Expected value: 140
print(get_h_m(t1))  # Expected value: 2, 20
