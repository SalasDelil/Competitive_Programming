class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        j  = n - 2
        stack = [n - 1]
        answer = [0]*n
        while j >= 0:
            if temperatures[stack[-1]] > temperatures[j]:
                answer[j] = stack[-1] - j
                stack.append(j)
                j -= 1
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(j)
                    j -= 1
                
        return answer