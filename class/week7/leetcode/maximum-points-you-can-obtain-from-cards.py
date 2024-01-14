class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = sum(cardPoints[:k])
        sum_ = max_sum
        left, right = k-1, len(cardPoints)-1

        while left >= 0:
            sum_ += (-cardPoints[left] + cardPoints[right])
            max_sum = max(max_sum, sum_)
            left -= 1
            right -= 1
        
        return max_sum