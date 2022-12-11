class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            subArray = nums[l[i]:r[i] + 1]
            subArray.sort()
            count = 0
            for j in range(1, len(subArray) - 1):
                if subArray[j] - subArray[j - 1] == subArray[-1] - subArray[-2]:
                    count += 1
                
            if count == len(subArray) - 2:
                answer.append(True)
            else:
                answer.append(False)
        return answer
