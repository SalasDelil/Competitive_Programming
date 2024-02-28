# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.mx = root.val
        self.mn = root.val
        self.ans = 0

        def difference(root, mx, mn):
            if not root:
                return

            self.ans = max(max(self.ans, abs(mx-root.val)), max(self.ans, abs(mn-root.val)))
            mx = max(mx, root.val)
            mn = min(mn, root.val)

            difference(root.left,mx,mn)
            difference(root.right,mx,mn)
            
        difference(root, self.mx, self.mn)
        return self.ans