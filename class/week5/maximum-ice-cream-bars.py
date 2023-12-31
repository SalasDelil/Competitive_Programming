class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_ice_cream_bars = 0
        costs.sort()
        for cost in costs:
            if cost <= coins:
                coins -= cost
                max_ice_cream_bars += 1
            else:
                break
        return max_ice_cream_bars