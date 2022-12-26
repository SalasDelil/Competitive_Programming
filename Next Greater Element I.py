class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in range(len(nums1)):
            stack.append(nums1[i])
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if stack[-1] < nums2[j]:
                    ans.append(nums2[j])
                    stack.pop()
                    break
                elif j == len(nums2) - 1:
                    ans.append(-1)
                    stack.clear()
        return ans
