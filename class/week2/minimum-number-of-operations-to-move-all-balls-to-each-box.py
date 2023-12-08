class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        ones_indices = [i for i in range(len(boxes)) if boxes[i] == "1"]

        left, right = 0, len(ones_indices)
        tot_moves = sum(ones_indices)
        j = 0
        answer.append(tot_moves)
        for i in range(1, len(boxes)):
            if j < len(ones_indices) and i > ones_indices[j]:
                j += 1
                left += 1
                right -= 1
                tot_moves -= (right - left)
            else:
                tot_moves -= (right - left)
            
            answer.append(tot_moves)

        return answer