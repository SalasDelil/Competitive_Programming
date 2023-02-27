class Solution:
    def removeDuplicates(self, s: str) -> str:
        dup = [s[-1]]
        ans = ''
        for i in range(2, len(s) + 1):
            if len(dup) != 0 and dup[-1] == s[-i]:
                dup.pop()
            else:
                dup.append(s[-i])
        
        n = len(dup)
        for i in range(n):
            ans += dup[-1]
            dup.pop()
        
        return ans
        