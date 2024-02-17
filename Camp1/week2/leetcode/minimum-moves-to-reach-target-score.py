class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        if maxDoubles == 0:
            return target - 1
        
        minMoves = 0

        while target > 1:
            if maxDoubles > 0:
                maxDoubles -= 1
                minMoves += target%2
                target //= 2
                minMoves += 1
            else:
                minMoves += target-1
                break

        return minMoves