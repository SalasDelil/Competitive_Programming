class Solution:
    def romanToInt(self, s: str) -> int:
        sym = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        n = len(s)
        i, j = 0, 1

        if n == 1:
            return sym[s[0]]

        while j < n:
            if sym[s[i]] > sym[s[j]]:
                if i == j - 1:
                    ans += sym[s[i]] + sym[s[j]]
                elif sym[s[j]] <= sym[s[j - 1]]:
                    ans += sym[s[j]]
                else:
                    ans += sym[s[j]] - 2*sym[s[j - 1]]
                j += 1
            elif sym[s[i]] == sym[s[j]] and sym[s[i]] == sym[s[j - 1]]:
                if i == j - 1:
                    ans += sym[s[i]] + sym[s[j]]
                else:
                    ans += sym[s[j]]
                j += 1
            else:
                if i == j - 1:
                    ans += sym[s[j]] - sym[s[i]]
                else:
                    ans += sym[s[j]] - 2*sym[s[j - 1]]
                i = j + 1
                j = i + 1
                if j == n:
                    ans += sym[s[i]]

            
        return ans