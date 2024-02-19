class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = odds = 0
        nice_subarrs = 0
        c, r, reven = 0, 0, []

        for i in range(n):
            if nums[i]%2==0: 
                c += 1
            else:
                reven.append(c)
                c = 0
        reven.append(c)

        while right <= n:
            if odds == k:
                nice_subarrs += (1 + reven[r])
                if nums[left]%2 != 0:
                    odds -= 1
                left += 1
                continue
            elif right < n and nums[right]%2 != 0:
                odds += 1
                r += 1

            right += 1
         
        return nice_subarrs
                