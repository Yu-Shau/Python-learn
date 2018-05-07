class Nstr(str):
    def __new__(cls, string):
        return str.__new__(cls, string)
    
    def __sub__(self, other):   #重写减法函数
        temp = self.replace(other, "")  #返回temp,self和other不变
        return temp

    def __rshift__(self, other):
        temp = self[-other:] + self[:-other]
        return temp

    def __lshift__(self, other):
        temp = self[other:] + self[:other]
        return temp

    def __add__(self, other):
        temp_self = 0
        temp_other = 0
        for each in self:
            temp_self += ord(each)
        for each in other:
            temp_other += ord(each)
        return temp_self + temp_other

    def __sub__(self, other):
        temp_self = 0
        temp_other = 0
        for each in self:
            temp_self += ord(each)
        for each in other:
            temp_other += ord(each)
        return temp_self - temp_other

    def __mul__(self, other):
        temp_self = 0
        temp_other = 0
        for each in self:
            temp_self += ord(each)
        for each in other:
            temp_other += ord(each)
        return temp_self * temp_other

    def __truediv__(self, other):
        temp_self = 0
        temp_other = 0
        for each in self:
            temp_self += ord(each)
        for each in other:
            temp_other += ord(each)
        return temp_self / temp_other

    def __floordiv__(self, other):
        temp_self = 0
        temp_other = 0
        for each in self:
            temp_self += ord(each)
        for each in other:
            temp_other += ord(each)
        return temp_self // temp_other
