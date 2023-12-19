class Solution:
    def minimizedStringLength(self, s: str) -> int:
        chars = [s[i] for i in range(len(s))]

        for i in range(1, len(chars)):
            if chars[i] != "":
                if chars[i] in chars[:i]:
                    ind = chars[:i].index(chars[i])
                    chars[ind] = ""

                if chars[i] in chars[i+1:]:
                    ind = chars[i+1:].index(chars[i])
                    chars[i+ind+1] = ""
        
        return len("".join(chars))