class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = nums.copy()
        answer = []
        for i in range(1, len(nums)):
            postfix[-i - 1] *= postfix[-i]
        for j in range(len(nums)):
            if j == 0:
                answer.append(postfix[j + 1])
            elif j == len(nums) - 1:
                prefix *= nums[j - 1]
                answer.append(prefix)
            else:
                prefix *= nums[j - 1]
                answer.append(postfix[j + 1]*prefix)
        
        return answer