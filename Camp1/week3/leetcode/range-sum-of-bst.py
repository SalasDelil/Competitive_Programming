# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        
        def add(node):
            if node:
                if low <= node.val <= high:
                    self.ans += node.val
                add(node.left)
                add(node.right)
            return self.ans
        return add(root)