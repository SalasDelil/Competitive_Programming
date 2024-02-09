class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(digit) for digit in s]
        n = len(nums)
        presum = [0]
        summ = 0
        
        for i in range(n):
            summ += nums[i]
            presum.append(summ)

        right  = presum[-1]
        max_score = 0

        for j in range(1, n):
            left = j - presum[j]
            temp = left + (right - presum[j])
            max_score = max(max_score, temp)

        return max_score
