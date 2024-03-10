class Solution:

    def counter(self, y: int, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.counter(y, -n)

        if n%2 == 0:
            return self.counter((y*y)%self.MOD, n//2)
        else:
            return y*self.counter((y*y)%self.MOD, (n-1)//2)

    def countGoodNumbers(self, n: int) -> int:
        self.MOD = 10**9 + 7
        odds = n // 2
        evens = n // 2 + n%2
        return (self.counter(5, evens)%self.MOD * self.counter(4, odds)%self.MOD)%self.MOD
