def BrokenHeart(userName):
    distinctChars = []
    for char in userName:
        if char not in distinctChars:
            distinctChars.append(char)
    if len(distinctChars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
name = input()
BrokenHeart(name)
