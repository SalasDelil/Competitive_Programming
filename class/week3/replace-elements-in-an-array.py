class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_dict = {nums[i]:i for i in range(len(nums))}

        for operation in operations:
            if operation[0] in nums_dict:
                nums[nums_dict[operation[0]]] = operation[1]
                nums_dict[operation[1]] = nums_dict[operation[0]]
        
        return nums