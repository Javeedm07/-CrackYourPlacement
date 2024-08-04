"""
Intuition:
This code defines a class `MyQueue` that implements a queue using a list. The `push` method adds an element to the front of the list, the `pop` method removes and 
returns the last element (mimicking a queue's FIFO behavior), the `peek` method returns the last element without removing it, and the `empty` method checks if the 
queue is empty.
"""

class MyQueue:
    def __init__(self):
        self.queue = []
      
    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
