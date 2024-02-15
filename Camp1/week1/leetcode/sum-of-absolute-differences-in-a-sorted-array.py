class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        totsum = sum(nums)
        presum = 0

        for i in range(n):
            leftdiff = abs(i*nums[i]-presum)
            rightdiff = abs(totsum - nums[i] - presum - nums[i]*(n-i-1))
            result.append(leftdiff + rightdiff)
            presum += nums[i]
        
        return result