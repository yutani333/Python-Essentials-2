class WeekDayError(Exception):
    pass

exit = 0
class Weeker:
    __weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        i = 0
        for item in Weeker._Weeker__weekdays:
            i += 1
            if item == day:
                self.day = i
                return

        raise WeekDayError

    def __str__(self):
        return Weeker._Weeker__weekdays[self.day-1]

    def add_days(self, n):
        self.day += n
        if self.day > 7:
            self.day = self.day % 7

    def subtract_days(self, n):
        self.day -= n
        if self.day < 1:
            self.day = 7 - (self.day % 7)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
