# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        rem = length%k
        divs = length//k
        temp = head
        parts = []

        for i in range(k):
            if not temp:
                parts.append(None) 
            else:
                parts.append(temp)
                cr = divs + 1 if rem > 0 else divs
                rem -= 1
                
                for j in range(cr - 1):
                    temp = temp.next  
                next_node = temp.next
                temp.next = None  
                temp = next_node  
                
        return parts