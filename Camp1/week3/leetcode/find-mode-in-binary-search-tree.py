# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.mx_cnt = 0
        self.count = 0
        self.val = -999

        def mode(node):
            if not node:
                return
                    
            mode(node.left)
            if self.val == node.val:
                self.count += 1
            else:
                self.count = 0
                self.val = node.val
            
            if self.mx_cnt < self.count:
                self.ans.clear()
                self.ans.append(node.val)
            elif self.mx_cnt == self.count:
                self.ans.append(node.val)
            self.mx_cnt = max(self.mx_cnt, self.count)

            mode(node.right)

            return self.ans
        
        return mode(root)