class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)   
        rabbits = 0

        for val in counts:
            if val == 0:
                rabbits += counts[val]
            elif counts[val] <= val + 1:
                rabbits += val + 1
            else:
                rabbits +=  (ceil(counts[val]/(val+1)) * (val + 1))
                
        return rabbits