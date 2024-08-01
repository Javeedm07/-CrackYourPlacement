"""
Intuition:
The code iterates through the linked list, using two pointers, `prev` and `curr`. When it encounters a sequence of nodes with the same value, it skips all these 
duplicates by advancing `curr` to the end of the sequence and linking `prev.next` to `curr.next`. If no duplicates are found, it simply advances both pointers. The 
use of a dummy node helps handle edge cases gracefully, ensuring the correct head of the modified list is returned.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next
