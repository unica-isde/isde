#!/usr/bin/env python
minutes_in_hour = 60


def create_time_slot(h=0, m=0):
    time_slot = {'h': h, 'm': m}
    return time_slot


def set_h_m(time_slot, h, m):
    time_slot['h'] = h
    time_slot['m'] = m


def set_m(time_slot, m):
    time_slot['h'] = int(m / minutes_in_hour)
    time_slot['m'] = m % minutes_in_hour


def get_h_m(time_slot):
    return time_slot['h'], time_slot['m']


def get_m(time_slot):
    return time_slot['h'] * minutes_in_hour + time_slot['m']


t1 = create_time_slot()

set_h_m(t1, 2, 20)
print(get_m(t1))  # Expected value: 140
print(get_h_m(t1))  # Expected value: 2, 20

set_m(t1, 140)
print(get_m(t1))  # Expected value: 140
print(get_h_m(t1))  # Expected value: 2, 20
