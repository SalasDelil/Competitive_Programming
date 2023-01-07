class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        closest_points = []
        
        for i in range(n):
            distance = (points[i][0])**2 + (points[i][1])**2
            points[i].insert(0, distance)
        
        points.sort()
        for j in range(n):
            if j < k:
                points[j].pop(0)
                closest_points.append(points[j])
            else:
                points[j].pop(0)
        
        return closest_points