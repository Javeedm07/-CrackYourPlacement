"""
Intuition:
The code reverses a segment of a linked list between positions `left` and `right`. It first converts the entire linked list to a Python list. It then reverses 
the sublist from `left` to `right` within the Python list. Finally, it updates the linked list nodes with the modified values from the Python list and returns 
the modified linked list.
"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        l = l[ : left - 1] + (l[left - 1 : right])[ : : -1] + l[right : ]
        ptr = head
        for i in range(len(l)):
            ptr.val = l[i]
            ptr = ptr.next
        return head
