class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goodidx = n-1

        for i in range(n-2, -1, -1):
            if goodidx - i <= nums[i]:
                goodidx = i
        
        if goodidx == 0:
            return True
        else:
            return False
