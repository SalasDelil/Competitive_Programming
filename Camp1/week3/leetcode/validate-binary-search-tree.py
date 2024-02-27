# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.in_order = float("-inf")

        def validate(root):
            if not root:
                return True

            left = validate(root.left)
            if root.val > self.in_order:
                self.in_order = root.val
            else:
                return False

            right =  validate(root.right)
            
            return left and right

        return validate(root)