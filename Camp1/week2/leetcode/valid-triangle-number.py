class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        ans = 0

        for i in range(2, len(nums)):
            left, right = 0, i-1
            count = 0

            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    count += right-left
                    right -= 1
                else:
                    left += 1
                    
            ans += count
                
        return ans