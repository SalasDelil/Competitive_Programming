class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deq = deque(sorted(deck))
        res = deque()
        n = len(deq)
        
        while n != len(res):
            temp = deq.pop()
            
            if len(res)>0:
                r = res.pop()
                res.appendleft(r)
            res.appendleft(temp)

        return res