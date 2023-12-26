class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 1

        for ele in arr2:
            while j < len(arr1):
                if ele == arr1[i]:
                    i += 1
                    j = i + 1
                elif ele == arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                    i += 1
                    j = i + 1
                else:
                    j += 1
            j = i + 1
        
        while i < len(arr1):
            for l in range(i + 1, len(arr1)):
                if arr1[i] > arr1[l]:
                    arr1[i], arr1[l] = arr1[l], arr1[i]
            i += 1
        
        return arr1

                    