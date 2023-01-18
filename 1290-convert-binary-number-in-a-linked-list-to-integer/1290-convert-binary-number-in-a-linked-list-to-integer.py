# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        current = head
        decimal = 0
        for i in range(length):
            if current.val == 1:
                decimal += 2**(length - i - 1)
                current = current.next
            else:
                current = current.next

        return decimal