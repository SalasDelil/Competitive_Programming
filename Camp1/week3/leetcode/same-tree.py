# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not(p or q):
                return True

            if p and q and (p.val == q.val):
                    return isSame(p.left, q.left) and isSame(p.right, q.right)

        return isSame(p, q)