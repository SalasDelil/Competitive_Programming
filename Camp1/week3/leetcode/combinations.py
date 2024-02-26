class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.path = []

        def combinations(m):
            if len(self.path) == k:
                self.ans.append(self.path.copy())
                return
            
            for i in range(m+1, n+1):
                self.path.append(i)
                
                combinations(i)

                self.path.pop()

        combinations(0)
        return self.ans