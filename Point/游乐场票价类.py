class Ticket:
    __price = 100

    def Cadult(self, num = 0, holiday = False):
        if(holiday):
            return self.__price * 1.2 * num
        else:
            return self.__price * num

    def Cchild(self, num = 0, holiday = False):
        if(holiday):
            return self.__price * 0.5 * 1.2 * num
        else:
            return self.__price * 0.5 * num

t = Ticket()
price = t.Cadult(2) + t.Cchild(1)
