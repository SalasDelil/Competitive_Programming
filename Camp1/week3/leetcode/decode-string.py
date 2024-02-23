class Solution:
    def decodeString(self, s: str) -> str:
        def decode(idx=0):
            subs = []
            curnum = 0

            while idx < len(s):
                if s[idx].isdigit():
                    curnum = curnum * 10 + int(s[idx])
                elif s[idx] == '[':
                    decsub, idx = decode(idx + 1)
                    subs.append(max(curnum, 1) * decsub)
                    curnum = 0
                elif s[idx] == ']': 
                    break
                else: 
                    subs.append(s[idx])
                idx += 1

            return ''.join(subs), idx
            
        return decode()[0]