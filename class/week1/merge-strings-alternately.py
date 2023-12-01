class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        n = min(w1, w2)
        merged_str = ""

        for i in range(n):
            merged_str += word1[i]
            merged_str += word2[i]
        
        if w1 > w2:
            merged_str += word1[w2:]
        else:
            merged_str += word2[w1:]

        return merged_str