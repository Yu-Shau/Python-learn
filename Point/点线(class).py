import math as m
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def set(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    def gety(self):
        return self.__y

class Line():
    def __init__(self, A = Point(0, 0), B = Point(0, 0)):
        self.__a = A
        self.__b = B
        
    def seta(self, x, y):
        self.__a.set(x, y)
    def setb(self, x, y):
        self.__b.set(x, y)
        
    def get_length(self):
        return m.sqrt((self.__a.getx() - self.__b.getx()) ** 2 +
                      (self.__a.gety() - self.__b.gety()) ** 2)
