class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        
        for i in range(n):
            if s[i] == "(":
                stack.append(0)
            else:
                top = stack.pop()
                if stack:
                    stack[-1] += max(2*top, 1)
                else:
                    stack.append(max(2*top, 1))
        
        return stack[0]