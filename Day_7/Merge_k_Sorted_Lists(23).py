"""
Intuition:
The code collects all the values from the given k linked lists into a single list, sorts the values, and then constructs a new sorted linked list from these sorted 
values. This approach ensures that the final linked list is in ascending order. Although simple and easy to understand, this method involves extra space for storing 
the node values and requires sorting the values, which may not be the most efficient approach for large datasets.
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [[]]:
            return None
        l = []
        for i in lists:
            head = i
            while head:
                l.append(head.val)
                head = head.next
        l.sort()
        head = None
        for i in l:
            if head:
                a = ListNode(i)
                t.next = a
                t = t.next
            else:
                head = ListNode(i)
                t = head
        return head
