class Stack:
    temp = []

    def isEmpty(self):
        if(len(self.temp) == 0):
            return True
        else:
            return False

    def push(self, data):
        self.temp.append(data)

    def pop(self):
        return self.temp.pop()

    def top(self):
        return self.temp[len(self.temp) - 1]

    def bottom(self):
        return self.temp[0]

    def __del__(self):
        del self.temp.clear()
