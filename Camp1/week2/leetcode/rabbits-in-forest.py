class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)   
        rabbits = 0

        for key in counts:
            if key == 0:
                rabbits += counts[key]
            elif counts[key] <= key + 1:
                rabbits += key + 1
            else:
                rabbits +=  (ceil(counts[key]/(key+1)) * (key + 1))
                
        return rabbits