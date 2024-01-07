class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        intersec = []

        if n == 0 or m == 0:
            return []

        for pair in firstList:
            ptr = 0

            while ptr < m:
                if pair[1] >= secondList[ptr][0] and pair[0] <= secondList[ptr][1]:
                    intersec.append([max(secondList[ptr][0], pair[0]), min(secondList[ptr][1], pair[1])])

                ptr += 1
                    
        return intersec
