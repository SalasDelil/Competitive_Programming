class Solution:
    def mySqrt(self, x: int) -> int:
        n = x//2
        for i in range(n + 2):
            if i*i == x:
                return i
            elif i*i > x:
                return i - 1