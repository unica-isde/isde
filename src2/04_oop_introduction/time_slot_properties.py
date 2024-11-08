class TimeSlot:
    """A class to store timeslots"""
    _minutes_in_hour = 60

    def __init__(self, name="a generic timeslot", m=0):
        self.name = name
        self._h = 0
        self._m = 0

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, m):
        """if m > 60 I do not change the value"""
        if m >= self._minutes_in_hour:  # 60
            print("You put a value >= 60. The original value remains unchaged")
        else:
            self._m = m

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    def __repr__(self):
        return "h:" + str(self.h) + " m:" + str(self.m)

    def __add__(self, t):
        m = self.m + t.m  # 30 + 40
        h = self.h + t.h + int(m / self._minutes_in_hour)
        m = m % self._minutes_in_hour
        new_ts = TimeSlot()
        new_ts.m = m
        new_ts.h = h
        return new_ts


if __name__ == "__main__":
    t1 = TimeSlot("Carbonara")
    t1.m = 20

    t2 = TimeSlot("Tiramisu")
    t2.m = 30

    t_menu = t1 + t2
    print("t_menu-> ", t_menu.h, t_menu.m)
