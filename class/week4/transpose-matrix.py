class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        columns = len(matrix[0])
        rows = len(matrix)

        transpose = [[0]*rows for _ in range(columns)]

        for row in range(len(matrix)):
            for col in range(columns):
                transpose[col][row] = matrix[row][col]
        
        return transpose
