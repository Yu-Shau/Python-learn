class Nstr(str):
    def __init__(self, string = ""):
        self.string = string

    def __lt__(self, other):
        temp_self = self.split(" ", 1)[0]
        temp_other = other.split(" ", 1)[0]
        if(len(temp_self) < len(temp_other)):
            return True
        else:
            return False
