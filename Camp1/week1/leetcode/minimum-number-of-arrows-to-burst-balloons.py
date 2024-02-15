class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        l, r = points[0][0], points[0][1]
        min_arrows = 1

        for i in range(1, len(points)):
            if r < points[i][0]:
                min_arrows += 1
                l = points[i][0]
                r = points[i][1]
                continue

            if points[i][0] > l and r >= points[i][0]:
                l = points[i][0]

            if r > points[i][1] and r > points[i][0]:
                r = points[i][1]
            
        return min_arrows