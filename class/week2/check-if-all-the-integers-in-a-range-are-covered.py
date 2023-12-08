class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_set = {item for item in range(left, right + 1)}
        range_sets = set()

        for rng in ranges:
            range_sets = range_sets.union({item for item in range(rng[0], rng[-1] + 1)})
        
        return my_set <= range_sets