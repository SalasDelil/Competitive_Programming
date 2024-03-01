class Solution:
    def trap(self, height: List[int]) -> int:
        tot_water = 0
        stack = []


        for right in range(len(height)):

            while stack and stack[-1][1] < height[right]:
                h = stack.pop()[1]
                
                if stack:
                    left, left_bound = stack[-1]
                    min_bound = min(height[right], left_bound)
                    tot_water +=  (right - left - 1)*(min_bound-h)

            stack.append([right, height[right]])

        return tot_water