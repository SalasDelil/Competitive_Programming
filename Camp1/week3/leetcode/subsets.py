class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for k in range(n+1):
            def backtrack(idx=0, curr=[]):
                if len(curr) == k:
                    result.append(curr[:])
                    return

                for i in range(idx, n):
                    curr.append(nums[i])
                    backtrack(i+1, curr)
                    curr.pop()

            backtrack()
        return result