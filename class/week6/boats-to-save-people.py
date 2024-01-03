class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minNumOfBoats = 0
        i, j = 0, len(people) - 1

        while i <= j:
            if people[i] + people[j] <= limit:
                minNumOfBoats += 1
                i += 1
                j -= 1
            else:
                minNumOfBoats += 1
                j -= 1
                
        return minNumOfBoats