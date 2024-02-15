class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        longestlen = 0
        firstOdd = False

        for val in counts.values():
            if val % 2 != 0 and not firstOdd:
                firstOdd = True
                longestlen += val
            else:
                temp = val % 2
                longestlen += val - temp

        return longestlen