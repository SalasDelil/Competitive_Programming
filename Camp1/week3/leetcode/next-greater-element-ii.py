class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        nxt_grtr = []

        for i in range(n):
            j = i
            while True:
                j = (j+1)%n
                if nums[j]>nums[i]:
                    nxt_grtr.append(nums[j])
                    break
                elif j == i:
                    nxt_grtr.append(-1)
                    break
        
        return nxt_grtr