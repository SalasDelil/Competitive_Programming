class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = defaultdict(int)
        longestLen = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in chars:
                chars[s[right]] = right
                longestLen = max(longestLen, right - left + 1)
            else:
                if chars[s[right]] >= left:
                    longestLen = max(longestLen, right - left)
                    left = chars[s[right]] + 1
                else:
                    longestLen = max(longestLen, right - left + 1)
                    
                chars[s[right]] = right
        
        return longestLen