# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        previousNode, currentNode = head, head

        while currentNode:
            if previousNode == currentNode:
                currentNode = currentNode.next
                previousNode.next = None
            else:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode

        return previousNode
