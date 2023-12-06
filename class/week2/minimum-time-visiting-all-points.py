class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tot_time = 0

        for i in range(len(points) - 1):
            xdiff = abs(points[i][0] - points[i+1][0])
            ydiff = abs(points[i][1] - points[i+1][1])
            
            tot_time += max(xdiff, ydiff)
        
        return tot_time
