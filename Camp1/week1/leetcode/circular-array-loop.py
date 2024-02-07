class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()

        for i in range(n):
            if i not in visited:
                temp_set = set()

                while True:
                    if i in temp_set:
                        return True
                    if i in visited:
                        break

                    visited.add(i)
                    temp_set.add(i)
                    prev, i = i, (i + nums[i]) % n

                    if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                        break

        return False