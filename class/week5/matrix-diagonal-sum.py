class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        tot_sum = 0
        n = len(mat)

        for i in range(n):
            tot_sum += mat[i][i]
        print(tot_sum)
        if n % 2 == 0:
            for i in range(n):
                tot_sum += mat[i][n - i - 1]
        else:
            for i in range(n):
                if i != n // 2:
                    tot_sum += mat[i][n - i - 1]
        
        return tot_sum
