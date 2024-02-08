class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)

        for book in bookings:
            first = book[0]
            last = book[1]
            seats = book[2]

            ans[first-1] += seats
            ans[last] += -seats
        
        for i in range(1, n):
            ans[i] += ans[i-1]

        ans.pop()

        return ans