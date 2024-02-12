# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictA = {}
        currA = headA

        while currA:
            dictA[currA] = currA.val
            currA = currA.next

        currB = headB

        while currB:
            if currB in dictA:
                return currB
            currB = currB.next
        
        