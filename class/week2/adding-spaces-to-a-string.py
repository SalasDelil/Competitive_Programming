class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []

        l=0

        for i in spaces:

            ans.append(s[l:i])
            ans.append(" ")
            l=i
        ans.append(s[i:])

        return "".join(ans)