"""
Intuition:
The code flattens a multi-level linked list where each node has a `next` pointer and a `bottom` pointer. It first traverses the list, collecting all node values in 
a list `l`, then sorts the values. Finally, it creates a new flattened list by inserting these sorted values as nodes linked through the `bottom` pointers. The 
result is a single-level linked list where nodes are sorted in ascending order.
"""

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

class Solution:
    def flatten(self, root):
        #Your code here
        l = []
        temp = root
        ptr = temp
        while ptr:
            while ptr:
                l.append(ptr.data)
                ptr = ptr.bottom
            ptr = temp.next
            temp = temp.next
        l.sort()
        dummy = Node(0)
        ans = dummy
        for i in l:
            a = Node(i)
            dummy.bottom = a
            dummy = dummy.bottom
        return ans.bottom
