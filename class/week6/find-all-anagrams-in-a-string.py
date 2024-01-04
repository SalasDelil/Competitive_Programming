class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        cnt_s = Counter(s[:m - 1])
        cnt_p = Counter(p)
        ans = []

        for i in range(m-1, n):
            cnt_s[s[i]] = cnt_s.get(s[i],0) + 1
            if cnt_s == cnt_p:
                ans.append(i - m + 1)

            cnt_s[s[i -m + 1]] -= 1
            if cnt_s[s[i -m + 1]] == 0:
                del cnt_s[s[i - m + 1]]

        return ans


        