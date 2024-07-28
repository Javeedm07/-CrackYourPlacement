"""
Intuition:
The code detects if a singly linked list has a cycle using the two-pointer technique. It initializes two pointers, `slow` and `fast`, both starting at the head of 
the list. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time. If the `slow` and `fast` pointers ever meet, a cycle is 
detected, and the function returns `True`. If the `fast` pointer reaches the end of the list, the function returns `False`, indicating no cycle.
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
