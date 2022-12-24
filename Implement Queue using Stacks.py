class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, y: int) -> None:
        self.stack.append(y)

    def pop(self) -> int:
        if len(self.stack) != 0:
            return self.stack.pop(0)

    def peek(self) -> int:
        if len(self.stack) != 0:
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
