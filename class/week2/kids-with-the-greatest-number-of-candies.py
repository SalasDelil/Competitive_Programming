class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        n = len(candies)
        max_ = max(candies)

        for i in range(n):
            if candies[i] + extraCandies >= max_:
                result.append(True)
            else:
                result.append(False)
        return result