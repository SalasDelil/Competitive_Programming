class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []

        def generator(op, cp):
            if op == cp == n:
                result.append("".join(curr))
                return

            if op < n:
                curr.append("(")
                generator(op+1,cp)
                curr.pop()
            if cp < op:
                curr.append(")")
                generator(op,cp+1)
                curr.pop()

        generator(0,0)

        return result