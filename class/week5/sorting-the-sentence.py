class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        words.sort(key=lambda word: word[-1])
        
        return " ".join(word[:len(word) - 1] for word in words)