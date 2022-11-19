class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        numstr = ''
        for i in range(len(num)):
            numstr += str(num[i])
        
        numint = int(numstr)
        sm = numint + k
        numstr = str(sm)
        result = []
        for j in range(len(numstr)):
            result.append(int(numstr[j]))
        
        return result
