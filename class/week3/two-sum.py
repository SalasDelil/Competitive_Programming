class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[i]:i for i in range(len(nums))}

        for i in range(len(nums)):
            if target - nums[i] in nums_dict and i != nums_dict[target - nums[i]]:
                return [i, nums_dict[target - nums[i]]]