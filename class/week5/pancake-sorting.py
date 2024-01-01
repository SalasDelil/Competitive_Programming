class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)

        for i in range(n):
            max_ = 0
            max_ind = 0
            for j in range(n-i):
                if arr[j] > max_:
                    max_ = arr[j]
                    max_ind = j
            
            k = max_ind+1
            flips.append(k)
            flips.append(n-i)

            subarr = arr[:k][::-1]
            arr = subarr + arr[k:]

            subarr  = arr[0:n-i][::-1]
            arr = subarr + arr[n-i:]

        return flips