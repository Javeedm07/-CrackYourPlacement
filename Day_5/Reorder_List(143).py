"""
Intuition:
The code reorders a linked list by alternating nodes from the beginning and the end. It first converts the linked list into a Python list for easy access. Using 
two pointers, it alternates setting the values of the linked list nodes from the start and end of the list. Finally, it updates the linked list nodes with these 
reordered values, ensuring the correct sequence.
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        ptr = head
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        left = 0
        right = len(l) - 1
        ptr = head
        while left < right:
            ptr.val = l[left]
            ptr.next.val = l[right]
            left += 1
            right -= 1
            ptr = ptr.next.next
        if ptr:
            ptr.val = l[left]
        return head
