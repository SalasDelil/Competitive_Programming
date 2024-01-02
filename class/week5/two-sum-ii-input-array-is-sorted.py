class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers) - 1

        while ind1 < ind2:
            if numbers[ind1] + numbers[ind2] == target:
                return [ind1 + 1, ind2 + 1]
            elif numbers[ind1] + numbers[ind2] > target:
                ind2 -= 1
            else:
                ind1 += 1
    