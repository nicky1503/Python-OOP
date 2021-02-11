import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        t = (self.hours, self.minutes, self.seconds)
        return '{:02}:{:02}:{:02}'.format(int(self.hours), int(self.minutes), int(self.seconds))

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        if self.hours == 24:
            self.hours = 0

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())


time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

