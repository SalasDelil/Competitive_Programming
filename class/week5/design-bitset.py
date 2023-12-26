class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = {i:"0" for i in range(self.size)}
        self.bitsetInv = {i:"1" for i in range(self.size)}
        self.ones = 0
        
    def fix(self, idx: int) -> None:
        if self.bitset[idx] == "0":
            self.bitset[idx] = "1"
            self.bitsetInv[idx] = "0"
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == "1":
            self.bitset[idx] = "0"
            self.bitsetInv[idx] = "1"
            self.ones -= 1

    def flip(self) -> None:
        self.ones = self.size - self.ones
        self.bitset, self.bitsetInv = self.bitsetInv, self.bitset

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        bits = self.bitset.values()
        return "".join(bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()