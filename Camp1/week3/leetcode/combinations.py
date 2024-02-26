class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def combinations(m):
            if len(path) == k:
                ans.append(path.copy())
                return
            
            for i in range(m+1, n+1):
                path.append(i)
                combinations(i)
                path.pop()

        combinations(0)
        return ans