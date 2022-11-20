class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        mult = 1
        
        while mult > 0:
            if (n*mult)%2 == 0:
                return n*mult
            mult += 1
