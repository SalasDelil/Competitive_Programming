class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        time_taken = 0

        while tickets[k] != 0:
            if tickets[0] != 0:
                time_taken += 1

                if k == 0:
                    k = n - 1
                else:
                    k -= 1
                    
                tickets.append(tickets[0]-1)
            else:
                k -= 1
                tickets.append(0)
            tickets.pop(0)
        
        return time_taken
                

