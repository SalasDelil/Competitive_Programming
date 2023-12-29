class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)-1
        operations = 0

        for i in range(n-1, -1, -1):
            if nums[i] != nums[i+1]:
                operations += n-i

        return operations
