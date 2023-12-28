class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        ans = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i + j] += [mat[i][j]]

        for key in diagonals.keys():
            if key % 2 != 0:
                ans += diagonals[key]
            else:
                diag = diagonals[key]
                ans += diag[::-1]

        return ans