class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        mx_per = 0

        for i in range(1, len(nums)-1):
            if nums[i] + nums[i-1] > nums[i+1] and nums[i] + nums[i+1] > nums[i-1] and  nums[i-1] + nums[i+1] > nums[i]:
                mx_per = max(mx_per, nums[i] + nums[i-1] + nums[i+1])
        
        return mx_per
