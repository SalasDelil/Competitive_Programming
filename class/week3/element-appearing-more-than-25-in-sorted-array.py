from math import ceil
from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        min_occurance = 0.25*n
        nums_count = Counter(arr)

        for key, value in nums_count.items():
            if value > min_occurance:
                return key
