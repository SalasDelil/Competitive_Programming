class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            count = nums.count(target)
            i = nums.index(target)
            return [i, i + count - 1]
                
        else:
            return [-1, -1]