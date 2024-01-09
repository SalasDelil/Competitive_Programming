class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        left, right = 0, k
        ans = count
        
        while right < len(s):
            if s[right] in vowels:
                count += 1

            if s[left] in vowels:
                count -= 1
            
            ans = max(count, ans)
            right += 1
            left += 1
        
        return ans