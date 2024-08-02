"""
Intuition:
The code adds two numbers represented by linked lists `l1` and `l2`, where each node contains a single digit, and the digits are stored in forward order. It converts 
the linked lists into integer numbers (`n1` and `n2`) by traversing each list and accumulating the digits. The sum of these integers is then converted to a string, and 
a new linked list is constructed from this string, digit by digit. The result is returned as a new linked list representing the sum.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        n1, n2 = 0, 0
        while p1 != None:
            n1 = n1 * 10 + p1.val
            p1 = p1.next
        while p2 != None:
            n2 = n2 * 10 + p2.val
            p2 = p2.next
        ans = str(n1 + n2)
        dummy = ListNode(0)
        curr = dummy
        for i in ans:
                curr.next = ListNode(i)
                curr = curr.next
        return dummy.next
