from sys import path
path.append("..\..\modules")
from debugA import bprint
from math import floor, ceil

class Timer:
    def __init__(self, hr = 0, min = 0, sec = 0):
        self.hr = self.min = self.sec = 0
        if hr in range(24):
            self.hr = hr
            if min in range(60):
                self.min = min
                if sec in range(60):
                    self.sec = sec
    
    def __str__(self):
        return formatTime(self.hr, self.min, self.sec)

    def next_second(self, inc = 1):
        self.sec += int(inc)
        if self.sec > 59:
            self.min += floor(self.sec/60)
            self.sec = self.sec % 60
            if self.min > 59:
                self.hr += floor(self.min/60)
                self.min = self.min % 60
                if self.hr > 23:
                    self.hr = self.hr % 24

    def prev_second(self, dec = 1):
        self.sec -= int(dec)
        if self.sec < 0:
            self.min += ceil(self.sec/60) - 1
            self.sec = 60 - (-self.sec % 60)
            if self.min < 0:
                self.hr += ceil(self.min/60) - 1
                self.min = 60 - (-self.min % 60)
                if self.hr < 0:
                    self.hr = 24 - (-self.hr % 24)


def formatTime(hr, min, sec):
    display = ""
    if hr < 10:
        display += "0"
    display += str(hr) + ":"
    if min < 10:
        display += "0"
    display += str(min) + ":"
    if sec < 10:
        display += "0"
    display += str(sec)
    
    return display

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

timer.next_second(input("How many seconds more? "))
print(timer)
timer.prev_second(input("How many seconds less? "))
print(timer)
