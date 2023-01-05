class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        j = 0
        intervals.sort()
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged_intervals[j][1] >= intervals[i][0] and merged_intervals[j][1] <= intervals[i][1]:
                merged_intervals[j][1] = intervals[i][1]
            elif merged_intervals[j][1] > intervals[i][1]:
                continue
            else:
                merged_intervals.append(intervals[i])
                j += 1
        
        return merged_intervals
