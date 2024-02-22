class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        for i in range(n):
            temp = costs[i][0] - costs[i][1]
            costs[i].append(temp)

        costs.sort(key= lambda cost: cost[2])
        min_cost = 0
        
        for j in range(n):
            if j < n//2:
                min_cost += costs[j][0]
            else:
                min_cost += costs[j][1]

        return min_cost