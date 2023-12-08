class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        i = -1
        while i >= -n:
            if int(num[n + i]) % 2 != 0:
                return num[:n + i + 1]
            else:
                i -= 1

        return ''