def countingSort(arr):
    freq_arr = [0]*100
    for i in range(0, len(arr)):
        freq_arr[arr[i]] += 1
    return freq_arr
