def insertionSort1(n, arr):
    m = arr[n - 1]

    for i in range(0, n):
        if m >= arr[n - (i + 2)]:
            arr[n - (i + 1)] = m
            print(*arr)
            break
        elif m < arr[n - (i + 2)]:
            if i == n - 1:
                arr[0] = m
                print(*arr)
                break
            arr[n - (i + 1)] = arr[n - (i + 2)]
            print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
