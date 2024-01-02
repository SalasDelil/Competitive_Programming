class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) > 0:
            l_ptr = nums.index(0)
            r_ptr = l_ptr + 1
            
            while r_ptr < len(nums):
                if nums[r_ptr] != 0:
                    nums[l_ptr], nums[r_ptr] = nums[r_ptr], nums[l_ptr]
                    l_ptr += 1
                    r_ptr += 1
                else:
                    r_ptr += 1
            
        return nums