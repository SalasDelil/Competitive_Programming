class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        n = len(candies)

        for i in range(n):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result