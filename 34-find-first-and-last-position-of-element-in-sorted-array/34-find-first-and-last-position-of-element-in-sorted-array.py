class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            c = nums.count(target)
            return [nums.index(target), nums.index(target) + c - 1]
                
        else:
            return [-1, -1]