class TimeSlot:
    """A class to store time slot"""
    minutes_in_hour = 60

    def __init__(self):  # initialize an empty slot
        self.timeslot = {'h': 0, 'm': 0}
        # timeslot is an instance attribute
        # (attribute of the object)

    def set_h_m(self, h, m):
        # set_h_m() is an instance method #(method of the object)
        self.timeslot['h'] = h
        self.timeslot['m'] = m

    def set_m(self, m):
        self.timeslot['h'] = int(m / self.minutes_in_hour)
        self.timeslot['m'] = m % self.minutes_in_hour

    def get_h_m(self):
        return self.timeslot['h'], self.timeslot['m']

    def get_m(self):
        return self.timeslot['h'] * self.minutes_in_hour + self.timeslot['m']


t1 = TimeSlot() # t1 is an object

t1.set_h_m(2, 20)
print(t1.get_m())  # Expected value: 140
print(t1.get_h_m())  # Expected value: 2, 120

t1.set_m(140)
print(t1.get_m())  # Expected value: 140
print(t1.get_h_m())  # Expected value: 2, 120
