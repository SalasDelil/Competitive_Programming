class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        l = len(strs[0])
        for s in strs:
            l = min(l, len(s))
        
        ans = ''
        for i in range(l):
            temp = strs[0][i]
            for j in range(n):
                if temp == strs[j][i]:
                    pass
                else:
                    return ans

            ans += temp

        return ans
        