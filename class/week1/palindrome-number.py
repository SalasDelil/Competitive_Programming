class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            nums = []
            while x >= 10:
                nums.append(x % 10)
                x -= x % 10
                x = x // 10
            nums.append(x)

            return nums == nums[::-1]