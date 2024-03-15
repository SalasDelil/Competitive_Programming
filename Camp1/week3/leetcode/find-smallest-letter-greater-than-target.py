class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        low = 0
        high = N-1
        
        if ord(target) >= ord(letters[high]) or ord(target) < ord(letters[low]):
            return letters[0]

        while low < high:
            mid = low + (high-low)//2

            if ord(letters[mid]) > ord(target):
                high = mid
            else:
                low = mid+1

        return letters[high]