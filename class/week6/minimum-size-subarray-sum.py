class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float("inf")
        ans =  INF
        subArrSum = 0
        left = 0

        for right in range(len(nums)):
            subArrSum+= nums[right]

            while left <= right and  subArrSum>=target:
                ans=min(right - left + 1, ans)
                subArrSum-=nums[left]
                left+=1

        return ans if ans != INF else 0
