class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self._count = [[x, 0] for x in args]

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self._count[key][1] += 1
        return self.values[key]

    def __setitem__(self, key, value):
        self._count[key][1] += 1
        self.values[key] = value
        self._count[key][0] = value

    def __delitem__(self, key):
        del self._count[key]
        del self.values[key]

    def append(self, value):
        self.values.append(value)
        self._count.append([value, 0])

    def pop(self):
        self.values.pop()
        self._count.pop()

    def remove(self, value):
        for each in range(len(self.values)):
            if(value == self.values[each]):
                temp = self._count[each][1]
        self.values.remove(value)
        self._count.remove([value, temp])

    def extend(self, value):
        self.values.extend(value)
        self._count.extend([x, 0] for x in value)

    def counter(self, index):
        return self._count[index][1]

    def insert(self, key, value):
        self.values.insert(key, value)
        self._count.insert(key, [value, 0])

    def clear(self):
        self.values.clear()
        self._count.clear()

    def reverse(self):
        self.values = self.values[::-1]
        self._count = self._count[::-1]
