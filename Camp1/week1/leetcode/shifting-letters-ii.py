class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0]*(len(s)+1)

        for left,right,dir in shifts:
            if dir:
                pref[left] += 1
                pref[right+1] -=1
            else:
                pref[left] -= 1
                pref[right+1] +=1

        res = ""
        summ = 0
        for i in range(len(s)): 
            summ += pref[i]
            res += chr(ord("a")+(ord(s[i])-ord("a")+summ)%26)
        return res