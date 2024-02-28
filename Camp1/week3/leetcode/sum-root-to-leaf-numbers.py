# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def find(node , string):
            if not node.left and not node.right:
                string += str(node.val)
                print(string)
                self.ans += int(string)
                return
            string += str(node.val)
            if node.left:
                find(node.left , string)
            if node.right:
                find(node.right , string)        
        find(root , '')
        return self.ans

