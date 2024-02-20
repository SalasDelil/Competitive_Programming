class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverser(s, l, r):
            if l >= r:
                return
                
            s[l], s[r] = s[r], s[l]
            return reverser(s, l+1, r-1)

        l, r = 0, len(s)-1
        reverser(s, l, r)