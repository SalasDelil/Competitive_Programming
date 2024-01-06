class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()

        for i in range(n):
            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                if nums[left] + nums[right] == target:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        
        return ans
        
   