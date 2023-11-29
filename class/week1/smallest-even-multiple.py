class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = n
        while i > 0:
            if i % 2 == 0 and i % n == 0:
                return i
            i += 1