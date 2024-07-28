"""
Intuition:
The code removes duplicates from a sorted singly linked list. It initializes two pointers, `temp1` and `temp2`, starting at the head and the second node, respectively.
It traverses the list, comparing the current nodes' values. If they differ, both pointers are moved forward. If they are the same, `temp2` is moved forward, and 
`temp1`'s `next` pointer is updated to skip the duplicate. The modified list without duplicates is then returned.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head .next == None:
            return head
        temp1 = head
        temp2 = head.next
        while temp2 != None:
            if temp1.val != temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                temp2 = temp2.next
                temp1.next = temp2
        temp1.next = None
        return head
