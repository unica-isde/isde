class TimeSlot:
    """A class to store time slot"""
    minutes_in_hour = 60

    def __init__(self, name='name'):  # initialize an empty slot
        self._h = 0
        self._m = 0
        self.name = name
        # timeslot is an instance attribute
        # (attribute of the object)

    @property
    def m(self):
        return self._m

    @property
    def h(self):
        return self._h

    @m.setter
    def m(self, m):
        self._h = int(m / self.minutes_in_hour)
        self._m = m % self.minutes_in_hour

    def set_h_m(self, h, m):
        # set_h_m() is an instance method #(method of the object)
        self._h = h
        self._m = m

    def get_h_m(self):
        return self._h, self._m

    def __add__(self, ts):
        new_ts = TimeSlot()
        new_ts.m = (self._h + ts._h) * self.minutes_in_hour + self._m + ts._m
        return new_ts


t1 = TimeSlot('Carbonara')
t1.m = 20

t2 = TimeSlot('Tiramisu')
t2.m = 30

t_menu = t1 + t2

print('t_menu-> ', t_menu.h, t_menu.m)
