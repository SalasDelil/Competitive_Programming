class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, -1
        max_area = 0
        while i - j < n:
            if height[i]  <= height[j]:
                if max_area < height[i]*(n - i + j):
                    max_area = height[i]*(n - i + j)
                i += 1
            else:
                if max_area < height[j]*(n - i + j):
                    max_area = height[j]*(n - i + j)
                j -= 1
        
        return max_area
