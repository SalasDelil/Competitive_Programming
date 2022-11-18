# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(None)
        n = 0
        curr = head
        while curr:
            n +=1
            curr = curr.next
        mid = n//2 + 1 
        curr = head
        while curr:
            if mid > 1:
                curr = curr.next
                mid -= 1
            else:
                dummyNode = curr
                break
        return dummyNode
