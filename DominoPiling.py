def maxDominos(size):
    values = size.split(" ")
    max_dom = (int(values[0]) * int(values[1]))//2
    return max_dom


size = input()
result = maxDominos(size)
print(result)
