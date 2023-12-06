class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest_perimeter = 0
        nums_len = len(nums)
        nums.sort(reverse=True)

        for i in range(nums_len - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                largest_perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                return largest_perimeter
        
        return largest_perimeter