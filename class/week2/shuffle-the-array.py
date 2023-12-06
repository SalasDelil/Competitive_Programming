class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(1, n):
            for j in range(n - i):
                nums[n - j + i - 2], nums[n - j + i - 1] = nums[n - j + i - 1], nums[n - j + i - 2]
        
        return nums