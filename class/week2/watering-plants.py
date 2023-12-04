class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        n = len(plants)
        cap = capacity
        i = 0
        while i < n:
            if capacity >= plants[i]:
                capacity -= plants[i]
                i += 1
                if i != n:
                    steps += 1
            else:
                steps -= 1
                steps += i
                capacity = cap
                steps += i + 1
        
        return steps
