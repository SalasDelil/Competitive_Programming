class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()

        while n > 0:
            sum_ = 0
            while n > 0:
                i = n%10
                sum_ += i*i
                n = n//10

            if sum_ == 1:
                return True

            if sum_ in sums:
                return False
            else:
                sums.add(sum_)

            n = sum_

        return False