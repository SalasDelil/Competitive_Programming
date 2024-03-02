class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        prefx = defaultdict(list)
        postfx = defaultdict(list)

        for i in range(n):
            if nums[i] in prefx:
                c, sm = prefx[nums[i]]
                ans[i] += (c*i - sm)
                prefx[nums[i]][0] += 1
                prefx[nums[i]][1] += i
            else:
                prefx[nums[i]] = [1, i]

            j = n-i-1
            if nums[j] in postfx:
                c2, sm2 = postfx[nums[j]]
                ans[j] += abs(sm2 - c2*j)
                postfx[nums[j]][0] += 1
                postfx[nums[j]][1] += j
            else:
                postfx[nums[j]] = [1, j]

        return ans