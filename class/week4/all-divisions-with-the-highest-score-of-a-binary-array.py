class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        division_scores = defaultdict(list)
        ones,zeros ,max_sum, i  = nums.count(1), 0, 0, 0

        while i < len(nums):
            sum_ = 0
            if nums[i] == 1:
                sum_ = ones + zeros
                max_sum = max(max_sum, sum_)
                division_scores[sum_] += [i]
                ones -= 1
            else:
                sum_ = ones + zeros
                max_sum = max(max_sum, sum_)
                division_scores[sum_] += [i]
                zeros += 1
            
            if i + 1 == len(nums) and nums[i] == 0:
                sum_ = ones + zeros
                max_sum = max(max_sum, sum_)
                division_scores[sum_] += [i + 1]

            i += 1

        return division_scores[max_sum]