"""
Intuition:
The code sorts a linked list by first converting it into a Python list to leverage Python's efficient built-in sort function. It iterates through the linked list 
to store node values in a list, sorts this list, and then iterates through the linked list again to update each node with the sorted values. Finally, it returns the 
sorted linked list.
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        l.sort()
        ptr = head
        for i in range(len(l)):
            ptr.val = l[i]
            ptr = ptr.next
        return head
