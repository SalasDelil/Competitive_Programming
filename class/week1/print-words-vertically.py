class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split()
        n = len(words)
        l = max((len(words[i]) for i in range(n)))

        for i in range(l):
            temp = ''
            for j in range(n):
                if len(words[j]) - i > 0:
                    temp += words[j][i]
                else:
                    temp += ' '
            
            ans.append(temp.rstrip())

        return ans