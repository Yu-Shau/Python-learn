class MyRev:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return self

    def __next__(self):
        try:
            temp = self.string[-1]
            self.string = self.string[:-1]
        except IndexError:
            raise StopIteration
        return temp
