class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = 0
        ptr2 = 0

        while ptr1 <= len(name) and ptr2 < len(typed):
            if ptr1 < len(name) and typed[ptr2] == name[ptr1]:
                ptr2 += 1
                ptr1 += 1
            elif typed[ptr2] == name[ptr1-1] and ptr1 != 0:
                ptr2 += 1
            else:
                return False
            
        return ptr1 == len(name) and ptr2 == len(typed)