class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0]*k
        self.ans = float("inf")

        if len(cookies)== k:
            return max(cookies)

        def backtrack(indx, distribution):
            if indx >= len(cookies):
                self.ans = min(self.ans, max(distribution))
                return

            if max(distribution) > self.ans:
                return

            for i in range(k):
                distribution[i] += cookies[indx]
                backtrack(indx+1, distribution)
                distribution[i] -= cookies[indx]

        backtrack(0, distribution)
        return self.ans