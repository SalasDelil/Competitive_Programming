class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e", "6":"f", "7":"g", "8":"h", "9":"i", "10#":"j", "11#":"k", "12#":"l", "13#":"m", "14#":"n", "15#":"o", "16#":"p", "17#":"q", "18#":"r",  "19#":"s", "20#":"t", "21#":"u", "22#":"v", "23#":"w", "24#":"x", "25#":"y", "26#":"z"}

        n = len(s)
        ans = ""
        i, j = 0, 2
        while j < n:
            if s[j] == "#":
                ans += chars[s[i:j + 1]]
                i = j + 1
                j = i + 2
                if j >= n:
                    while i < n:
                        ans += chars[s[i]]
                        i += 1
                    return ans
            else:
                ans += chars[s[i]]
                i += 1
                j += 1
                if j >= n:
                    while i < n:
                        ans += chars[s[i]]
                        i += 1
                    return ans

        return ans
        