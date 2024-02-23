# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(l_root,r_root):
            if not l_root and not r_root: return True

            if l_root and r_root and (l_root.val == r_root.val):
                    return isSym(l_root.left, r_root.right) and isSym(l_root.right, r_root.left)
        
        return isSym(root.left, root.right)