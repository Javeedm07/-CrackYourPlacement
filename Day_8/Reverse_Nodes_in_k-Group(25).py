"""
Intuition:
The code reverses nodes of a linked list in groups of `k`. It first traverses the list to store the values in a list `l`. It then reverses the sublists of length `k` 
within `l`. After modifying `l` with the reversed sublists, it updates the original linked list nodes with the new values from `l`, thereby achieving the desired 
reordering of nodes in groups of `k`.
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        l = []
        ptr = head
        while ptr:
            l.append(ptr.val)
            ptr = ptr.next
        i = 0
        while i + k <= len(l):
            l[i : i + k] = l[i : i + k][ : : -1]
            i  += k
        ptr = head
        for i in l:
            ptr.val = i
            ptr = ptr.next
        return head
