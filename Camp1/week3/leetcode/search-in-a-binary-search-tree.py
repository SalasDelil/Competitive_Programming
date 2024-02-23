# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root):
            if root is None:
                return None

            if root.val > val:
                root.left = search(root.left)
                return root.left
                
            if root.val < val:
                root.right = search(root.right)
                return root.right

            if root.val == val:
                return root

        return search(root)