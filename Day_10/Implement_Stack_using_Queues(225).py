"""
Intuition:
This code defines a class `MyStack` that implements a stack using a deque. The `push` method adds an element to the front of the deque, the `pop` method removes and 
returns the first element, the `top` method returns the first element without removing it, and the `empty` method checks if the deque is empty.
"""
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue = deque((x, self.queue))

    def pop(self) -> int:
        value, self.queue = self.queue
        return value

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
 
