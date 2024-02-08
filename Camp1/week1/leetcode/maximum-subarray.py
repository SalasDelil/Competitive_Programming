class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        res, minval = float('-inf'), float('inf')

        for i in range(n):
            minval = min(minval, pre_sum[i])

            res = max(res, pre_sum[i + 1] - minval)

        return res