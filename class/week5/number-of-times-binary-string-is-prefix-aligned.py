class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_ = 0
        count = 0

        for i in range(len(flips)):
            max_ = max(max_, flips[i])
            if max_ == i + 1:
                count += 1
        
        return count