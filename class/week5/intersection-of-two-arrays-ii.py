class Solution:
    def sorter(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = self.sorter(nums1)
        nums2 = self.sorter(nums2)
        ans = []
        i, j = 0, 0

        while i < len(nums1):
            while j < (len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    j += 1
                    break
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    break
            
            i += 1

        return ans