class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if (m + n)%2 == 0:
            median = (nums[(n + m)//2 - 1] + nums[(n + m)//2]) / 2
            return median
        else:
            return nums[(n + m)//2]