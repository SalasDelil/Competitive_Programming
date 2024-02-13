# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        left, right = left-1, right-1
        n = right - left
        dmy = ListNode()
        dmy.next = head
        leftNode = dmy
        
        while left > 0:
            leftNode = leftNode.next
            left -= 1

        curr = leftNode.next
        leftend = curr
        prevNd = None

        while n >= 0:
            nextNode = curr.next
            curr.next = prevNd
            prevNd = curr
            curr = nextNode
            n -= 1
        
        leftNode.next = prevNd
        leftend.next = curr

        return dmy.next
        