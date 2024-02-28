# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.n = 0
        self.k = k
        self.ans = 0

        def find_smallest(root):
            if not root:
                return

            find_smallest(root.left)
            
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
                return root.val

            find_smallest(root.right)

        find_smallest(root)
        return self.ans