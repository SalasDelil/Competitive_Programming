class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0
        if sum(nums[1:]) == 0:
            return 0
        
        indx = 1
        leftsum = nums[0]
        rightsum = sum(nums[indx+1:])
        if leftsum == rightsum:
            return 1
        while indx < len(nums)-1:
            leftsum += nums[indx]
            rightsum -= nums[indx+1]
            indx += 1
            if leftsum == rightsum:
                return indx
        return -1