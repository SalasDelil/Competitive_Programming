class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
        "6":6, "7":7, "8":8, "9":9}
        n1 = 0
        n2 = 0
        for i in range(len(num1)):
            n1 += (10**i)*nums[num1[len(num1) - i - 1]]
        for i in range(len(num2)):
            n2 += (10**i)*nums[num2[len(num2) - i - 1]]
        
        ans = n1 * n2
        return str(ans)