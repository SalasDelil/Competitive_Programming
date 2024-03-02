class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm = sum(nums)
        if sm % p == 0:
            return 0

        prefixsum = 0
        rightmost_rem = {0: -1}
        ans = len(nums)

        for i, val in enumerate(nums):
            prefixsum = (prefixsum + val) % p
            r = (prefixsum - sm % p) % p

            if r in rightmost_rem:
                j = rightmost_rem[r]
                ans = min(ans, i - j)
            rightmost_rem[prefixsum] = i

        return ans if ans < len(nums) else -1