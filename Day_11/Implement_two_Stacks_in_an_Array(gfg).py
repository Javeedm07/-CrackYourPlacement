"""
Intuition:
This code defines a class `TwoStacks` that simulates two stacks within a single list. `push1` adds elements to the front of the list (for stack 1), and `push2` adds 
elements to the end of the list (for stack 2). `pop1` removes and returns the front element (from stack 1), and `pop2` removes and returns the last element 
(from stack 2). The class maintains counts of elements in each stack (`n1` for stack 1 and `n2` for stack 2) to manage operations correctly.
"""

class TwoStacks:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.arr = []
      
    def push1(self, x):
        self.arr.insert(0, x)
        self.n1 += 1

    def push2(self, x):
        self.arr.append(x)
        self.n2 += 1

    def pop1(self):
        if self.n1 == 0:
            return -1
        self.n1 -= 1
        return self.arr.pop(0)

    def pop2(self):
        if self.n2 == 0:
            return -1
        self.n2 -= 1
        return self.arr.pop()
