# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.mx_sm = 0

        def post_order(node):
            if not (node.left or node.right):
                self.mx_sm = max(self.mx_sm, node.val)
                return node.val, node.val, node.val

            left_sm, left_min, left_mx = 0, node.val, float("-inf")
            if node.left:
                left_sm, left_min, left_mx = post_order(node.left)
            
            right_sm, right_min, right_mx = 0, float("inf"), node.val
            if node.right:
                right_sm, right_min, right_mx = post_order(node.right)

            if left_mx < node.val < right_min:
                sm = left_sm + node.val + right_sm
                self.mx_sm = max(self.mx_sm, sm)
                return sm, left_min, right_mx
            else:
                return 0, float("-inf"), float("inf")
        
        post_order(root)
        return self.mx_sm
