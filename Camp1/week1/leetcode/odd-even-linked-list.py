# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fasthd = head.next
        fast = fasthd

        while fast and fast.next:
            slow.next = fast.next
            slow = slow.next
            fast.next = slow.next
            fast = fast.next

        slow.next = fasthd

        return head
