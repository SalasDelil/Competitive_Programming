class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        mxlen = len(set(nums))
        ans = left = 0
        cntdict = {}

        for right in range(n):
            cntdict[nums[right]] = cntdict.get(nums[right], 0) + 1

            while len(cntdict) == mxlen:
                ans += n - right
                cntdict[nums[left]] -= 1

                if cntdict[nums[left]] == 0:
                    del cntdict[nums[left]]
                left += 1
                        
        return ans