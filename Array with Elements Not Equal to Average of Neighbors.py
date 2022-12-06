class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums) - 1):
            if (nums[i - 1] + nums[i + 1]) / 2 != nums[i]:
                continue
            elif (nums[i - 1] + nums[i + 1]) / 2 == nums[i] and nums[i + 1] == nums[-1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                if (nums[i - 1] + nums[i - 3])/2 == nums[i - 2]:
                    nums[i - 1], nums[-1] = nums[-1], nums[i - 1]
                elif (nums[i - 2] + nums[i])/2 == nums[i - 1]:
                    nums[i - 1], nums[-1] = nums[-1], nums[i - 1]
            else:
                nums[i], nums[-1] = nums[-1], nums[i]
                if (nums[i - 2] + nums[i])/2 == nums[i - 1]:
                    nums[i - 1], nums[-1] = nums[-1], nums[i - 1]
                elif (nums[i - 1] + nums[i - 3])/2 == nums[i - 2]:
                    nums[i - 1], nums[-1] = nums[-1], nums[i - 1]
        return nums
