class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        minTime = 0
        processorTime.sort()
        tasks.sort(reverse=True)

        for i in range(len(processorTime)):
            finishTime = processorTime[i]+tasks[i*4]
            minTime = max(minTime, finishTime)
        
        return minTime