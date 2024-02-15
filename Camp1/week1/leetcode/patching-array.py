class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    sm, i, patches = 1, 0, 0

    while sm <= n:
        if i < len(nums) and nums[i] <= sm:
            sm += nums[i]
            i += 1
        else:
            sm *= 2
            patches += 1

    return patches