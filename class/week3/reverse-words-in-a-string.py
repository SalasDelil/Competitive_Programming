class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()

        return " ".join(words[::-1])
