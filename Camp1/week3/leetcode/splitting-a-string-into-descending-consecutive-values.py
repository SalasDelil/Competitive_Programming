class Solution:
    def splitString(self, s: str) -> bool:
        curr = []

        def backtrack(candidate):
            if candidate >= len(s):
                for j in range(1, len(curr)):
                    if curr[j-1] - curr[j] != 1:
                        return False
                return len(curr) >= 2

            for i in range(candidate, len(s)):
                val = int(s[candidate:i+1])
                if not curr and val == 0:
                    continue
                else:
                    curr.append(val)

                    if backtrack(i+1):
                        return True
                    curr.pop()

            return False

        return backtrack(0)

        # Time complexity n*2^n