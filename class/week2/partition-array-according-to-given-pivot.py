class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0]*len(nums)
        pivot_count = nums.count(pivot)
        left = 0

        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1

        right = pivot_count + left
        for j in range(len(nums)):
            if nums[j] > pivot:
                ans[right] = nums[j]
                right += 1
            elif nums[j] == pivot:
                ans[left] = pivot
                left += 1

        return ans
