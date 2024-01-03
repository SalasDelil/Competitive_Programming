class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_ptr, r_ptr = 0, 1

        while r_ptr < len(nums):
            if nums[l_ptr] == nums[r_ptr]:
                r_ptr += 1
            else:
                l_ptr += 1
                nums[l_ptr] = nums[r_ptr]
        print(nums)

        return l_ptr + 1