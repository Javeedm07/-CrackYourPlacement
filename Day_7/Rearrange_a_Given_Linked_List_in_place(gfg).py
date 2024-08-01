"""
Intuition:
The code reorders a linked list by first storing the node values in a list, then using two pointers (`left` and `right`) to set the values in the original linked list 
in a specific order: alternating between the start and end of the values list. This results in the reordered list where the first element is followed by the last 
element, the second element by the second last, and so on.
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        p1 = head
        p2 = head
        values = []
        while p2:
            values.append(p2.val)
            p2 = p2.next
        left, right = 0, len(values) - 1
        while left <= right:
            p1.val = values[left]
            p1 = p1.next
            if p1 is not None:
                p1.val = values[right]
                p1 = p1.next
            left += 1
            right -= 1
