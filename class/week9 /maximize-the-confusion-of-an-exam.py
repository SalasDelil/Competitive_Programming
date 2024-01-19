class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left, Ts, Fs = 0, 0, 0

        for right in range(n):
            if answerKey[right] == "T":
                Ts += 1
            else:
                Fs += 1

            if Ts > k and Fs > k:
                if answerKey[left] == "T":
                    Ts -= 1
                else:
                    Fs -= 1
                left += 1
        
        return n - left