class Solution(object):
    def numIdenticalPairs(self, nums):
        good_pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    good_pairs += 1
        return good_pairs
        
