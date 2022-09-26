class Solution:
    def sortColors(self, nums: List[int]) -> None:
        no_of_zeros = nums.count(0)
        no_of_ones = nums.count(1)
        no_of_twos = nums.count(2)
        
        nums.clear()
        for i in range(no_of_zeros):
            nums.append(0)
        for j in range(no_of_ones):
            nums.append(1)
        for k in range(no_of_twos):
            nums.append(2)
        
        return nums
