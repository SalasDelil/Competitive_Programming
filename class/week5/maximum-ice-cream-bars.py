class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ny_coins = 0
        costs.sort()

        for cost in costs:
            if cost <= coins:
                coins -= cost
                ny_coins += 1

        return ny_coins