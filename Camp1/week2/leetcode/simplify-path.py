class Solution:
    def simplifyPath(self, path: str) -> str:
        # iterate over the input
        # while iterating if we find another / we jump that iteration
        # if we find a . we append it

        temp = path.split('/')
        stack = []

        for val in temp:
            if(val == '..'):
                if(stack):
                    stack.pop()
            elif(val != '' and val != '.'):
                stack.append(val)
        if(stack):
            stack[0] = '/' + stack[0]
        else:
            return '/'
        res = "/".join(stack)

        return res