"""
Intuition:
The code adds two numbers represented by linked lists `l1` and `l2`. It iteratively sums corresponding digits from both lists along with any carry from the previous 
digit, creating new nodes for the result list. A dummy head node is used to simplify list construction, and the process continues until all digits and any remaining 
carry are processed. The resulting linked list represents the sum of the two input numbers in reverse order.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while p1 != None or p2 != None:
            s = carry
            if p1 != None:
                s += p1.val
                p1 = p1.next
            if p2 != None:
                s += p2.val
                p2 = p2.next
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next
