class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        left, right = 0, k - 1

        while left <= right:
            if nums[left] == val and nums[right] == val:
                right -= 1
                k -= 1
            elif nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
                k -= 1
            elif nums[left] != val and nums[right] == val:
                right -= 1
                k -= 1
            else:
                left += 1
        
        return k
            