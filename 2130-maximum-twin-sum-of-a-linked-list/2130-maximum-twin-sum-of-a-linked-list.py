# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        twin = []
        curr = head
        max_twin_sum = 0
        # length of the linked list
        while curr:
            n += 1
            curr = curr.next
        # find the max twin sum
        curr = head
        for i in range(n):
            if i <= n/2 - 1:
                twin.append(curr.val)
                curr = curr.next
            else:
                sm = twin[-1] + curr.val
                if max_twin_sum < sm:
                    max_twin_sum = sm
                twin.pop()
                curr = curr.next
                
        return max_twin_sum