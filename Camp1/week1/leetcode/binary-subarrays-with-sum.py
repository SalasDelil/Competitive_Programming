class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        tot_count = 0

        for i in range(1, n):
            nums[i] += nums[i-1]
        
        sum_dict = defaultdict()
        
        for j in range(n):
            if nums[j] == goal:
                tot_count += 1

            if nums[j] - goal in sum_dict:
                tot_count += sum_dict[nums[j]-goal]

            sum_dict[nums[j]] = sum_dict.get(nums[j], 0) + 1

        return tot_count