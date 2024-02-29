# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(nums):
            mx = max(nums)
            index = nums.index(mx)
            root = TreeNode(mx)
            root.left = construct(nums[:index]) if index > 0 else None
            
            root.right = construct(nums[index+1:]) if index < len(nums)-1 else None
            return root
            
        return construct(nums)
