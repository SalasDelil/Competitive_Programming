class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            xstr = str(x)
            y = xstr[::-1]
            x = int(y)
            if -2**31 <= x < 2**31:
                return x
            else:
                return 0
        else:
            xstr = str(-x)
            y = xstr[::-1]
            x = int(y)
            if -2**31 <= x < 2**31:
                return -x
            else:
                return 0
