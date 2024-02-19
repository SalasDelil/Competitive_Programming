class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
            
        chars = [char for char in palindrome]
        charset = set(chars)

        if len(charset) == 1:
            if chars[0] == "a":
                chars[-1] = "b"
            else:
                chars[0] = "a"
            return "".join(chars)

        for i in range(n):
            if n%2 == 0:
                if chars[i] != "a":
                    chars[i] = "a"
                    break
            else:
                if i==n//2:
                    if chars[i-1] != "z":
                        chars[-1] = "b"
                        break
                    elif chars[i-1] != "a":
                        chars[i-1] = "a"
                        break
                elif chars[i] != "a":
                    chars[i] = "a"
                    break
                
        return "".join(chars)
