# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        
        index = 0
        current = head
        if count == n:
            return head.next

        while current:
            if count - n - 1 == index:
                current.next = current.next.next
                return head
            else:
                index += 1
                current = current.next
                
        return head.next