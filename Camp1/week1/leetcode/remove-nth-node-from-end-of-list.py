# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode()
        dummy.next = head
        i = 1
        prev, curr = dummy, head

        while curr.next:
            if i == n:
                prev = prev.next
                curr = curr.next
            else:
                curr = curr.next
                i += 1

        prev.next = prev.next.next
        
        return dummy.next
