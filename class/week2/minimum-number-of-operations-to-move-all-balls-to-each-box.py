class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        ones_indices = [i for i in range(len(boxes)) if boxes[i] == "1"]

        for i in range(len(boxes)):
            temp_sum = 0
            for index in ones_indices:
                temp_sum += abs(i - index)

            answer.append(temp_sum)

        return answer