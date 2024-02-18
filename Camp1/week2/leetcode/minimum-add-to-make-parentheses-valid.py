class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        opening = {"(":")"}

        for par in s:
            if stack:
                if opening.get(stack[-1]) == par:
                    stack.pop()
                else:
                    stack.append(par)
            else:
                stack.append(par)
        
        return len(stack)