class Solution:
    def numberOfMatches(self, n: int) -> int:
        tot_matches = 0
        match = n
        while match > 1:
            if match % 2 == 0:
                match = match // 2 
                tot_matches += match
            else:
                match = match // 2 
                tot_matches += match
                match += 1

        return tot_matches