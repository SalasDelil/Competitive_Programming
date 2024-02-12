class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.count  = 0

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        
        curr = self.head
        
        while index >= 0:
            curr = curr.next
            index -= 1

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

        self.count += 1

    def addAtTail(self, val: int) -> None:
        prev = self.head
        curr = self.head.next

        while curr:
            prev = curr
            curr = curr.next

        tail_node = Node(val)
        prev.next = tail_node

        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        
        prev = self.head
        curr = self.head

        while index >= 0:
            prev = curr
            curr = curr.next
            index -= 1

        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        
        prev, curr = self.head, self.head

        while index >= 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        prev.next = curr.next
        self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)