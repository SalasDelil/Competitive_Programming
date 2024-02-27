class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        self.s = ["0"]

        def reverse_invert(s):
            for i in range(len(s)):
                if int(s[i]): s[i] = "0"
                else: s[i] = "1"
            return s[::-1]

        def binary_string(n, s):
            if n == 0:
                return self.s[k-1]
            
            self.s = self.s + ["1"] + reverse_invert(self.s)
            return binary_string(n-1, self.s)
    
        return binary_string(n-1, self.s)