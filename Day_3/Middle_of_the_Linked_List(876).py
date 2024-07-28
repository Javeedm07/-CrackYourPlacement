"""
Intuition:
The code finds the middle node of a singly linked list using the two-pointer technique. It initializes two pointers, `slow` and `fast`, both starting at the head 
of the list. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time. When the `fast` pointer reaches the end of the list, 
the `slow` pointer will be at the middle node, which is then returned.
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
