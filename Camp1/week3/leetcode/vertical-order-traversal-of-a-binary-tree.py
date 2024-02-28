# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        def traverse(node , y , x):
            if node:
                traverse(node.left , y - 1 , x + 1)
                self.ans[y].append([node.val , x])
                traverse(node.right , y + 1 , x + 1)
        traverse(root , 0 , 0)
        answer = []
        final = []
        keys = sorted(self.ans)

        for key in keys:
            answer.append(self.ans[key])

        for node in answer:
            node.sort(key = lambda x:x[-1])
            node = sorted(node , key=lambda x: (x[1], x[0]))
            new_list = []
            for i in range(len(node)):
                new_list.append(node[i][0])
            final.append(new_list)

        return final