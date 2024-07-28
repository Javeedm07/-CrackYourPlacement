"""
Intuition:
The code removes all nodes with a given value `val` from a singly linked list. It creates a dummy node pointing to the head to handle edge cases. It then uses two 
pointers, `prev` and `curr`, to traverse the list. If `curr.val` equals `val`, `prev.next` is updated to skip `curr`. Otherwise, both pointers are moved forward. 
Finally, the modified list starting from `node.next` (original head) is returned.
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head
        prev, curr = node, head
        while curr != None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return node.next
