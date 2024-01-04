class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum = sum(nums[:k])
        max_avg = _sum / k

        for i in range(k, len(nums)):
            _sum = _sum + nums[i] - nums[i-k]
            max_avg = max(max_avg, _sum / k)

        return max_avg