class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr_nums = [i * i for i in nums]
        sqr_nums.sort()
        return sqr_nums
