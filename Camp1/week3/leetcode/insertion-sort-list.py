# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 

        arr_list = []
        temp = head

        while temp is not None:
            arr_list.append(temp.val)
            temp = temp.next

        i = 0
        arr_list.sort()
        temp = head
        while temp is not None:
            temp.val = arr_list[i]
            i += 1
            temp = temp.next

        return head
        