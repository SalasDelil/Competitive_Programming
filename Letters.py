def Letters():
    t = int(input())
    if 1 <= t <= 1000:
        min_alphabets = []
        for i in range(t):
            x = 0
            n = int(input())
            if 1 <= n <= 100:
                message = input()
                for j in range(n):
                    if ord(message[j]) - 96 > x:
                        x = ord(message[j]) - 96
                min_alphabets.append(x)
            else:
                return
        for x in min_alphabets:
            print(x)
    else:
        return

Letters()
