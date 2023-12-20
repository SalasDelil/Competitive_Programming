class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                temp = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                max_sum = max(max_sum, temp)
        
        return max_sum