class Solution:
    def numberOfWays(self, s: str) -> int:
        nums = [0]
        n = len(s)
        summ = 0

        for j in range(n):
            summ += int(s[j])
            nums.append(summ)
        # print(nums)

        valid_ways = 0
        right = nums[-1]

        for i in range(1, n + 1):
            # count 101 pairs
            if s[i-1] == "0" and nums[i] != 0:
                valid_ways += nums[i]*(right - nums[i])
            
            # count 010 pairs
            if s[i-1] == "1":
                valid_ways += (i-nums[i])*((n - i) - (right - nums[i]))

        return valid_ways