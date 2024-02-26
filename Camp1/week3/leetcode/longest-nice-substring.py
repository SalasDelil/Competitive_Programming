class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        chars_set = set(s)

        for i in range(len(s)):
            if s[i].lower() not in chars_set or s[i].upper() not in chars_set:
                str1 = self.longestNiceSubstring(s[:i])
                str2 = self.longestNiceSubstring(s[i+1:])

                return max(str1, str2, key=len)

        return s