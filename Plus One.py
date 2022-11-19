class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numstr = ''
        n = len(digits)
        for i in range(n):
            numstr += str(digits[i])
        
        num = int(numstr)
        num = num + 1
        num = str(num)
        nums = []
        for i in num:
            nums.append(int(i))
        
        return nums
