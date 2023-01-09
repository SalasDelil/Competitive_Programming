class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        #for i in nums:
        #    if i == 0:
        #        nums.remove(i)
        #        nums.append(0)
        # but the followng is with better performance
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0 or nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
            else:
                j += 1
