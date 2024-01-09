class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 1
        count = 0
        prev = 0
        length = len(nums)

        if nums.count(0) == length:
            return  0
        elif nums.count(1) == length:
            return length - 1

        while right < length:
            if nums[left] == 0 and nums[right] == 1:
                count = max(count, prev + right - left)
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                count = max(count, prev + right - left - 1)
                prev = right - left - 1
                left = right
                right = left + 1
            elif nums[left] != 0:
                left += 1
                right = left + 1
                prev += 1

        return count