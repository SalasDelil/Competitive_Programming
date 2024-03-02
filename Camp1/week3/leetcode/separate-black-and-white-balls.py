class Solution:
    def minimumSteps(self, s: str) -> int:
        # 1-black and 0-white
        # 0...1 order

        # -------------- using two pointers ---------------
        # s_list = [val for val in s]
        # left = right = 0
        # steps = 0

        # while right < len(s_list):
        #     if s_list[left] == "1" and s_list[right] == "0":
        #         s_list[left], s_list[right] = s_list[right], s_list[left]
        #         steps += right - left
        #     elif s_list[left] == s_list[right] == "1":
        #         right += 1
        #         continue
        #     right += 1
        #     left += 1

        # return steps


        # ---------------- using prefix sum ---------------
        min_steps = ones = 0

        for color in s:
            if color == "1":
                ones += 1
            else:
                min_steps += ones
        
        return min_steps
