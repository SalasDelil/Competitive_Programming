class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0]*(1001)
        max_trip_length = 0

        for trip in trips:
            numPassengers = trip[0]
            frm = trip[1]
            to = trip[2]
            max_trip_length = max(max_trip_length, to)

            passengers[frm] += numPassengers
            passengers[to] += -numPassengers
        
        for i in range(1, 1001):
            if passengers[i-1] > capacity:
                return False

            passengers[i] += passengers[i-1]


        return True