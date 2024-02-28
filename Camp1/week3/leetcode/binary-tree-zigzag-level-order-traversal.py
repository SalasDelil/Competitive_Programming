# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.zigzag = []
        self.levels = defaultdict(list)
        self.depth = 0

        def zigzag_order(root):
            if not root:
                return

            self.levels[self.depth].append(root.val)
            self.depth += 1

            zigzag_order(root.left)
            zigzag_order(root.right)

            self.depth -= 1

        zigzag_order(root)

        for key, value in self.levels.items():
            if key % 2 == 0:
                self.zigzag.append(value)
            else:
                self.zigzag.append(value[::-1])
                
        return self.zigzag