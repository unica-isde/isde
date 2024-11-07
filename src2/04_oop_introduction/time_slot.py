class TimeSlot:
    """ DoCSTRING -> A class to store time slot"""

    def __init__(self, h=0, m=0):
        self.hours = h
        self.mins = m

    def set_m(self, m):
        self.hours = int(m / 60)
        self.mins = m % 60

    def set_h_m(self, h, m):
        self.hours = h
        self.mins = m

    def get_m(self):
        return self.hours * 60 + self.mins

    def get_h_m(self):
        return self.hours, self.mins
