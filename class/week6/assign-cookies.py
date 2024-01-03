class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pt1, pt2, max_content = 0, 0, 0

        while pt1 < len(g) and pt2 < len(s):
            if s[pt2] >= g[pt1]:
                max_content += 1
                pt1 += 1
                pt2 += 1
            else:
                pt2 += 1
        
        return max_content

