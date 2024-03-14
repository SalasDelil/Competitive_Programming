class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)

        if target < nums[0] or target > nums[-1]: return -1
        elif target == nums[0]: return 0
        elif target == nums[-1]: return N-1
        
        i = 0
        l, r = 0, N-1

        while l < r:
            i = l + (r-l)//2

            if nums[i] == target:
                return i
            elif target > nums[i]:
                l = i+1
            else:
                r = i
        
        return -1
