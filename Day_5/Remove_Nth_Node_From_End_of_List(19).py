"""
Intuition:
The code removes the nth node from the end of a linked list. It starts by creating a dummy node before the head to handle edge cases. It advances the head pointer 
by n steps, then moves both the head and dummy pointers together until head reaches the end. Finally, it skips the nth node by adjusting the next pointer of the dummy 
node and returns the modified list starting from the original head.
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res
        for _ in range(n):
            head = head.next
        while head:
            head = head.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return res.next
