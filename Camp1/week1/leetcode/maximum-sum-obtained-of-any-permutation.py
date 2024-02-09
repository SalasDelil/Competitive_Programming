class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        counts = [0]*n

        for request in requests:
            counts[request[0]] += 1

            if request[1] + 1 < n:
                counts[request[1] + 1] -= 1
        
        for i in range(1, n):
            counts[i] += counts[i - 1]
        
        counts.sort()
        nums.sort()
        ans = 0

        for j in range(n):
            ans += (counts[j] * nums[j])

        return ans % (10**9 + 7)