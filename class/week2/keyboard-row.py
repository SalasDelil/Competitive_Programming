class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        ans = []

        for i in range(len(words)):
            temp = ""
            for j in range(len(words[i])):
                if words[i][j].lower() in row1:
                    if temp == "":
                        temp = row1
                    elif temp != row1:
                        break
                    if j + 1 == len(words[i]):
                        ans.append(words[i])
                elif words[i][j].lower() in row2:
                    if temp == "":
                        temp = row2
                    elif temp != row2:
                        break
                    if j + 1 == len(words[i]):
                        ans.append(words[i])
                elif words[i][j].lower() in row3:
                    if temp == "":
                        temp = row3
                    elif temp != row3:
                        break
                    if j + 1 == len(words[i]):
                        ans.append(words[i])
        return ans