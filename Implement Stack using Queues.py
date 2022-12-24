class MyStack:

    def __init__(self):
        self.queues = []

    def push(self, y: int) -> None:
        self.queues.append(y)

    def pop(self) -> int:
        if len(self.queues) != 0:
            return self.queues.pop(-1)

    def top(self) -> int:
        if len(self.queues) != 0:
            return self.queues[-1]

    def empty(self) -> bool:
        return len(self.queues) == 0

    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(y)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
