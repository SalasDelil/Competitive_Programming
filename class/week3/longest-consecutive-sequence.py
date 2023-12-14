class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        longest_cons = 0

        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            print(count)
            if nums[i] - nums[i - 1] == 1:
                count += 1
            elif nums[i] == nums[i - 1]:
                pass
            else:
                longest_cons = max(count + 1, longest_cons)
                count = 0

            if i == len(nums) - 1:
                longest_cons = max(count + 1, longest_cons)

        return longest_cons