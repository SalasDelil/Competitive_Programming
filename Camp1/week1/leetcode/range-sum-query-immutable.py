class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            self.pre_sum.append(summ)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right+1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)