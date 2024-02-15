class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        longestlen = 0
        firstOdd = False

        for val in counts.values():
            if val % 2 != 0 and not firstOdd:
                firstOdd = True
                longestlen += val
            else:
                longestlen += 2*(val//2)
                
        return longestlen