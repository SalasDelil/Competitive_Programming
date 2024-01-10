class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        n = len(nums)
        for i in range(n):
            k -= 1 - nums[i]
            if k < 0:
                k += 1 - nums[j]
                j += 1
        return n - j