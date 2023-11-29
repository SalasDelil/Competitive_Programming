class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if (num - 3) % 3 == 0:
            n = (num - 3)//3
            for i in range(3):
                ans.append(n + i)
            return ans

        return ans