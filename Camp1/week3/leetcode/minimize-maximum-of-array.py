class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = cur_sum = 0

        for indx, num in enumerate(nums):            
            cur_sum += num

            if num > mx:
                mid_float = cur_sum / (indx + 1)
                mid_int = int(-1 * mid_float // 1 * -1)
                mx = max([mx, mid_int])

        return mx
