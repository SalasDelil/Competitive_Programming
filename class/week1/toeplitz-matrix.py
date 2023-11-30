class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        l = len(matrix[0])

        for i in range(1, m):
            for j in range(1, l):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        
        return True
            


        

        