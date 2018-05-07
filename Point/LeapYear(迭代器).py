import time as t
class LeapYear:
    def __init__(self):
        self.year = t.localtime()[0] + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.year -= 1
        while(not (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
            self.year -= 1
        return self.year
