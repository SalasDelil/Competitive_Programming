class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
        else:
            for i in range(len(intervals) + 1):
                if i < len(intervals) and intervals[i][0] >= newInterval[0]:
                    intervals.insert(i, newInterval)
                elif i == len(intervals):
                    intervals.append(newInterval)
        
        j = 0
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
