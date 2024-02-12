# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        curr = head
        stack = []
        if not head.next:
            return True
        while curr:
            length += 1
            curr = curr.next
        
        current = head
        i = 0
        while current:
            if i <= length//2 - 1:
                stack.append(current.val)
            elif length % 2 == 0 and stack[-1] == current.val:
                stack.pop()
            elif length % 2 != 0:
                length += 1
            else:
                return False
            i += 1
            current = current.next
        
        if len(stack) == 0:
            return True
        else:
            return False
            