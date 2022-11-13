class Solution: 
    def select(self, arr, i):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        return min
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minInd = self.select(arr, i)
            if minInd!=i:
                arr[minInd],arr[i] =arr[i],arr[minInd]
        return arr
