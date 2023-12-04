class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        i, j = 0, 2

        while j < len(num):
            if int(num[i]) == int(num[j]) and int(num[i]) == int(num[j - 1]):
                ans = max(ans, int(num[i:j + 1]))
            i += 1
            j += 1
        
        if ans > 0:
            return str(ans)
        elif ans == 0:
            return "000"
        else:
            return ""