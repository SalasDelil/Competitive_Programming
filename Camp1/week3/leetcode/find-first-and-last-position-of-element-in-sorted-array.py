class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        N = len(nums)
        low1 = 0
        high1 = N-1

        # starting position
        while low1 < high1:
            mid = low1 + (high1-low1)//2

            if nums[mid] >= target:
                high1 = mid
            else:
                low1 = mid+1

        low2 = 0
        high2 = N

        # ending position
        while low2 < high2-1:
            mid = low2 + (high2-low2)//2

            if nums[mid] > target:
                high2 = mid
            else:
                low2 = mid
                
        return [high1, low2] if nums[high1]==nums[low2]==target else [-1,-1]