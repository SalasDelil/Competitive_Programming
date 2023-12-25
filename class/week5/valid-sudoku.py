class Solution:
    def subBoxChecker(self, grid, row, col):
        sub_box = set()

        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if grid[i][j] != ".":
                    if grid[i][j] not in sub_box:
                        sub_box.add(grid[i][j])
                    else:
                        return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if self.subBoxChecker(board, i, j) == False:
                    return False
        
        for r in range(len(board)):
            sub_set1 = set()
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] not in sub_set1:
                        sub_set1.add(board[r][c])
                    else:
                        return False
        
        for co in range(len(board[0])):
            sub_set = set()
            for ro in range(len(board)):
                if board[ro][co] != ".":
                    if board[ro][co] not in sub_set:
                        sub_set.add(board[ro][co])
                    else:
                        return False

        return True