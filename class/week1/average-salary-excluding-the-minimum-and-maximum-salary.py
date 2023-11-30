class Solution:
    def average(self, salary: List[int]) -> float:
        mn = min(salary)
        mx = max(salary)
        sm = 0

        for i in range(len(salary)):
            if salary[i] != mn and salary[i] != mx:
                sm += salary[i]
        
        avg = sm / (len(salary) - 2)

        return avg