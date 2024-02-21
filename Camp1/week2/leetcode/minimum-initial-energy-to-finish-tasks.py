class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1]-task[0], reverse=True)
        min_energy = 0
        temp = 0

        for task in tasks: 
            if task[1] < temp:
                temp -= task[0]
            else:
                min_energy += task[1]-temp
                temp += (task[1]-temp)
                temp -= task[0]

        return min_energy