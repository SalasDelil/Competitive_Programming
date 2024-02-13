# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        prev, curr = None, head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        ans, i = 0, 0

        while prev:
            ans += prev.val*(2**i)
            prev = prev.next
            i += 1
        
        return ans