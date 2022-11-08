class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        
        for i in range(len(accounts)):
            wealthSum = 0
            for j in range(len(accounts[i])):
                wealthSum += accounts[i][j]
            if wealthSum >= maxWealth:
                maxWealth = wealthSum
        return maxWealth
