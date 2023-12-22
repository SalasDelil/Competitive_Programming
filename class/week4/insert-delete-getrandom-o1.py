class RandomizedSet:

    def __init__(self):
        self.myset = []
        self.indices = {}
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        else:
            self.indices[val] = self.i
            self.myset.append(val)
            self.i += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val]
            self.indices[self.myset[-1]] = index
            self.myset[index], self.myset[-1] = self.myset[-1], self.myset[index]
            self.myset.pop()
            self.indices.pop(val)
            self.i -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.myset)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()