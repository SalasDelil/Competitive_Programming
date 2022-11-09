class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = 0
        
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    n = i + 1
            return n
