class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = {}
        valid_ints = []
        least_count = n // 3

        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1

        for key, value in counts.items():
            if value > least_count:
                valid_ints.append(key)
        
        return valid_ints