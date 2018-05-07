class Nint(int):
    def __new__(cls, temp):
        if(isinstance(temp, str)):
            num = 0
            for each in temp:
                num += ord(each)
            return int.__new__(cls, int(num))
        else:
            return int.__new__(cls, int(temp))
