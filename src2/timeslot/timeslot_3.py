class TimeSlot:
    """A class to store time slot"""
    minutes_in_hour = 60

    def __init__(self, name='name'):  # initialize an empty slot
        self._timeslot = {'h': 0, 'm': 0}
        self.name = name
        # timeslot is an instance attribute
        # (attribute of the object)

    def set_h_m(self, h, m):
        # set_h_m() is an instance method #(method of the object)
        self._timeslot['h'] = h
        self._timeslot['m'] = m

    def set_m(self, m):
        self._timeslot['h'] = int(m / self.minutes_in_hour)
        self._timeslot['m'] = m % self.minutes_in_hour

    def get_h_m(self):
        return self._timeslot['h'], self._timeslot['m']

    def get_m(self):
        return self._timeslot['h'] * self.minutes_in_hour + self._timeslot['m']

    def add(self, ts):
        new_ts = TimeSlot()
        new_ts.set_m(self.get_m() + ts.get_m())
        return new_ts


t1 = TimeSlot('Carbonara')
t1.set_m(20)

t2 = TimeSlot('Tiramisu')
t2.set_m(30)

t_menu = t1.add(t2)

print(t_menu.get_h_m())
