class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums1)

        for i in range(len(nums1)):
            stack.append(nums1[i])
            indx = nums2.index(nums1[i])

            for j in range(indx, len(nums2)):
                print(stack)
                if stack[-1] < nums2[j]:
                    ans[i] = nums2[j]
                    stack.pop()
                    break
                elif j == len(nums2) - 1:
                    stack.clear()

        return ans