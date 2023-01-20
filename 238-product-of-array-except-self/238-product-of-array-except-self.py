class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums.copy()
        postfix = nums.copy()
        answer = []
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i - 1]
            postfix[-i - 1] *= postfix[-i]
        for j in range(len(nums)):
            if j == 0:
                answer.append(postfix[j + 1])
            elif j == len(nums) - 1:
                answer.append(prefix[j - 1])
            else:
                answer.append(postfix[j + 1]*prefix[j - 1])
        
        return answer