class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(':')', '[':']', '{':'}'}
        stack = []

        for i in range(len(s)):
            if len(stack)!=0 and parentheses.get(stack[-1]) == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return len(stack)==0