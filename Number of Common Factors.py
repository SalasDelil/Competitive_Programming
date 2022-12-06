class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        com_fact = 0
        if a >= b:
            for i in range(1, b + 1):
                if a%i == 0 and b%i == 0:
                    com_fact += 1
        elif a < b:
            for i in range(1, a + 1):
                if a%i == 0 and b%i == 0:
                    com_fact += 1
        return com_fact
