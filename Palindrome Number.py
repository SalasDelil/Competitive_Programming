class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        if n > 1:
            for i in range(n//2):
                if x[i] != x[-i - 1]:
                    return False
            return True
        else:
            return True
