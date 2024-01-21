class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_dict = defaultdict(str)
        most_frequent = 0
        left = 0
        max_len = 0

        for end, char in enumerate(s):
            chars_dict[char] = chars_dict.get(char, 0) + 1 
            most_frequent = max(most_frequent, chars_dict[char])
            
            if (end - left + 1) - most_frequent > k:
                chars_dict[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, end-left+1)
        
        return max_len