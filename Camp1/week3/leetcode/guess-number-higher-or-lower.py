# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            mid = low + (high-low)//2
            temp = guess(mid)

            if high-low == 1:
                if not guess(high):
                    return high
                else:
                    return low

            if temp == -1:
                high = mid
            elif temp == 1:
                low = mid
            else:
                return mid

        return 1