class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")", "[":"]", "{":"}"}
        c = 0
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) != 0 and brackets.get(stack[-1]) == s[i]:
                stack.pop()
                c += 1
            else:
                stack.append(s[i])
        return len(s)/2 == c
      
