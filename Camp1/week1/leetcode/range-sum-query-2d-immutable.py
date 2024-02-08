class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix[0])
        m = len(matrix)
        self.pre = [[0]*(n+1) for _ in range(m+1)]

        for r in range(m):
            for c in range(n):
                self.pre[r+1][c+1] = self.pre[r][c+1] + self.pre[r+1][c] - self.pre[r][c] + matrix[r][c]

        print(self.pre)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2+1][col2+1]-self.pre[row2+1][col1]-self.pre[row1][col2+1]+self.pre[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)