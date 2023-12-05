class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_path = sum([tar if tar>=0 else -tar for tar in target])
        for i in range(len(ghosts)):
            if abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1]) <= my_path:
                return False
            
        return True