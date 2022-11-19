class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        k = 1
        n1 = 0
        n2 = 0
        for i in range(len(num1)):
            if k == 1:
                n1 += nums[num1[-i - 1]]
                k *= 10
            else:
                n1 += nums[num1[-i - 1]]*k
                k *= 10
        t = 1
        for j in range(len(num2)):
            if t == 1:
                n2 += nums[num2[-j - 1]]
                t *= 10
            else:
                n2 += nums[num2[-j - 1]]*t
                t *= 10
                
        result = n1*n2
        
        return str(result)
