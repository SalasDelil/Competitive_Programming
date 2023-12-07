class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue

            count += 1
            if count > 1:
                return False

            if i > 0 and nums[i + 1] < nums[i - 1]:
                nums[i + 1] = nums[i]
            else:
                nums[i] = nums[i + 1]

        return True