class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start <= destination:
            if sum(distance[start:destination]) <= sum(distance) // 2:
                return sum(distance[start:destination])
            else:
                return sum(distance) - sum(distance[start:destination])
        else:
            if sum(distance[destination:start]) <= sum(distance) // 2:
                return sum(distance[destination:start])
            else:
                return sum(distance) - sum(distance[destination:start])