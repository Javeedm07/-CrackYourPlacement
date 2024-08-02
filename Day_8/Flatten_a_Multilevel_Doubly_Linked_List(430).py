"""
Intuition:
The code defines a function to flatten a multilevel doubly linked list. It iteratively traverses the list, and if a node has a child, it inserts the child between the 
current node and the next node, using a stack to keep track of the next nodes to be processed later. Once the child nodes are processed, it continues with the nodes 
from the stack, ensuring all levels are flattened into a single level. Finally, it returns the head of the modified list.
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        ptr = head
        while ptr:
            if ptr.child:
                if ptr.next:
                    stack.append(ptr.next)
                ptr.next = ptr.child
                ptr.next.prev = ptr
                ptr.child = None
            if ptr.next == None and len(stack) != 0:
                ptr.next = stack.pop()
                ptr.next.prev = ptr
            ptr = ptr.next
        return head
