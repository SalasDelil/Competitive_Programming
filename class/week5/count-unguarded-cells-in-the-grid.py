class Solution:
    def guardChecker(self, grid, m, n, guards):
        guardedcells = 0

        for guard in guards:
            for r in range(guard[0]+1, m):
                if grid[r][guard[1]] == ".":
                    grid[r][guard[1]] = "g"
                    guardedcells += 1
                elif grid[r][guard[1]] == "g":
                    continue
                else:
                    break

            for row in range(guard[0]-1,-1,-1):
                if grid[row][guard[1]] == ".":
                    grid[row][guard[1]] = "g"
                    guardedcells += 1
                elif grid[row][guard[1]] == "g":
                    continue
                else:
                    break

            for c in range(guard[1]+1, n):
                if grid[guard[0]][c] == ".":
                    grid[guard[0]][c] = "g"
                    guardedcells += 1
                elif grid[guard[0]][c] == "g":
                    continue
                else:
                    break

            for col in range(guard[1]-1,-1,-1):
                if grid[guard[0]][col] == ".":
                    grid[guard[0]][col] = "g"
                    guardedcells += 1
                elif grid[guard[0]][col] == "g":
                    continue
                else:
                    break

        return guardedcells

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [["."]*n for _ in range(m)]

        for i in range(len(guards)):
            grid[guards[i][0]][guards[i][1]] = "G"

        for j in range(len(walls)):
            grid[walls[j][0]][walls[j][1]] = "W"

        result = self.guardChecker(grid, m, n, guards)

        return m*n - result - len(guards) - len(walls)