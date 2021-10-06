from collections import deque


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        try:
            return self.queue[0]
        except IndexError:
            return None

    def empty(self) -> bool:
        return not bool(self.queue)
