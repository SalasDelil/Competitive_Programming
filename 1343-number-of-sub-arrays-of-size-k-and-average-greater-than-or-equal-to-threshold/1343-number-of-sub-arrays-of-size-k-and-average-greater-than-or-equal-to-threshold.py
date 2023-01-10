class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num_of_subArray = 0
        summation = 0
        for i in range(len(arr)):
            if i < k - 1:
                summation += arr[i]
            else:
                summation += arr[i]
                average = summation/k
                if average >= threshold:
                    num_of_subArray += 1
                summation -= arr[i - k + 1]
        
        return num_of_subArray