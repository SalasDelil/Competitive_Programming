class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pt1, pt2 = 0, 0

        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] == nums2[pt2]:
                return nums1[pt1]
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                pt2 += 1

        return -1