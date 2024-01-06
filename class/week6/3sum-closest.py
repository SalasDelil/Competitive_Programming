class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        sum_ = [float("inf"), 0]

        for i in range(n):
            left, right = i + 1, n - 1

            while left < right:
                temp = abs(nums[i] + nums[left] + nums[right] - target)

                if nums[i] + nums[left] + nums[right] < target:
                    if sum_[0] > temp:
                        sum_[0] = temp
                        sum_[1] = nums[i] + nums[left] + nums[right]
                    left += 1
                elif nums[i] + nums[left] + nums[right] > target:
                    if sum_[0] > temp:
                        sum_[0] = temp
                        sum_[1] = nums[i] + nums[left] + nums[right]
                    right -= 1
                else:
                    return nums[i] + nums[left] + nums[right]
        
        return sum_[1]
    
        