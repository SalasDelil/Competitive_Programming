class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = arr[0]
        dir = "up"

        if len(arr) < 3:
            return False
        elif arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        else:
            for i in range(1, len(arr) - 1):
                if arr[i] > peak and dir == "up":
                    peak = arr[i]
                elif arr[i] < peak:
                    peak = arr[i]
                    dir = "down"
                else:
                    return False

            return True
            