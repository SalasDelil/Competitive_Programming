class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # the last element should be considered the largest
        ans = 0
        n = len(nums)

        for i in range(n-2, -1, -1):            
            n = ceil(nums[i]/nums[i+1])
            nums[i] //= n
            ans += n-1
        
        return ans