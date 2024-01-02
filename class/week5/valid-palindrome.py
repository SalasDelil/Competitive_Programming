class Solution:
    def isPalindrome(self, s: str) -> bool:
        chrs = []
        
        for i in range(len(s)):
            if s[i].isalnum():
                chrs.append(s[i].lower())
        
        l_ptr, r_ptr = 0, len(chrs)-1

        while l_ptr < r_ptr:
            if chrs[l_ptr] != chrs[r_ptr]:
                return False
            
            l_ptr += 1
            r_ptr -= 1
        
        return True