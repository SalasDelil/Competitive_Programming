class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount = 0
        tenCount = 0

        for bill in bills:
            if bill == 5: 
                fiveCount += 1
            elif bill == 10:
                if fiveCount == 0:
                    return False
                tenCount += 1
                fiveCount -= 1
            else:
                if (fiveCount >= 1 and tenCount >= 1):
                    fiveCount-=1
                    tenCount-=1
                elif fiveCount>=3:
                    fiveCount-=3
                else:
                    return False
        return True