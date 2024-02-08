class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot_count = 0

        for i in range(1, n):
            nums[i] += nums[i-1]
        
        sum_dict = defaultdict()

        for j in range(n):
            if nums[j] % k == 0:
                tot_count += 1
            
            if nums[j] % k in sum_dict:
                tot_count += sum_dict[nums[j] %  k]

            sum_dict[nums[j]%k] = sum_dict.get(nums[j]%k, 0) + 1

        return tot_count