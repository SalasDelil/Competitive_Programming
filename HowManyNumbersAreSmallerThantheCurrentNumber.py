class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        numbers = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            numbers.append(count)
        return numbers
      
