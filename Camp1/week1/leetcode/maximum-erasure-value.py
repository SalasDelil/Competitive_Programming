class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numsIndices = defaultdict(int)
        numsIndices[nums[0]] = 0
        left, ans = -1, nums[0]

        for right in range(1, len(nums)):
            if nums[right] in numsIndices:
                left = max(left, numsIndices[nums[right]])
            
            numsIndices[nums[right]] = right
            nums[right] += nums[right-1]

            if left != -1:
                sub_arr_sum = nums[right] - nums[left]
            else:
                sub_arr_sum = nums[right]
            
            ans = max(ans, sub_arr_sum)
    
        return ans
