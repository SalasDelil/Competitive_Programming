class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sub_tbl = {}
        decoded_msg = ''
        i = 0
        a = 97
        while i < len(key):
            if key[i] not in sub_tbl and key[i] != ' ':
                sub_tbl[key[i]] = chr(a + i)
                i += 1
            elif key[i] == ' ' or key[i] in sub_tbl:
                i += 1
                a -= 1
        for char in message:
            if char != ' ':
                decoded_msg += sub_tbl[char]
            else:
                decoded_msg += ' '
        
        return decoded_msg