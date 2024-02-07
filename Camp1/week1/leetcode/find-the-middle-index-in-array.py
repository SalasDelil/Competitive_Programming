class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [0]
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            pre_sum.append(summ)
        pre_sum.append(0)

        for j in range(len(nums)):
            if pre_sum[j] == pre_sum[-2] - pre_sum[j+1]:
                return j

        return -1