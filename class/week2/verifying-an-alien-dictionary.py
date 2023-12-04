class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        chars = {order[i]: i for i in range(len(order))}

        for i in range(1,len(words)):
            a, b = words[i-1], words[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                achar, bchar = a[j], b[j]
                aindx, bindx = chars[achar], chars[bchar]
                if aindx < bindx:
                    break
                if aindx > bindx:
                    return False
        return True
                

                
