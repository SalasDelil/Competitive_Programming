class MyStack:

    def __init__(self):
        self.queues = []

    def push(self, y: int) -> None:
        self.queues.append(y)

    def pop(self) -> int:
        return self.queues.pop(-1)

    def top(self) -> int:
        return self.queues[-1]

    def empty(self) -> bool:
        return len(self.queues) == 0
