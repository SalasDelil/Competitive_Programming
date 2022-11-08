class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for val in ransomNote:
            if ransomNote.count(val) <= magazine.count(val):
                result = True
            else:
                result = False
                break
        return result
