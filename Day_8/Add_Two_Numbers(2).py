"""
Intuition:
The code adds two numbers represented by linked lists `l1` and `l2`, where each node contains a single digit and the digits are stored in reverse order. It converts
the linked lists into integer numbers (`n1` and `n2`) by traversing each list, multiplies each digit by the appropriate power of 10, and then sums these integers. 
The sum is then converted back to a string, reversed, and used to construct a new linked list representing the sum in reverse order. The result is returned as a 
new linked list.
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        n1, n2 = 0, 0
        x = 1
        while p1 != None:
            n1 = n1 + p1.val * x
            x = x * 10
            p1 = p1.next
        x = 1
        while p2 != None:
            n2 = n2 + p2.val * x
            x = x * 10
            p2 = p2.next
        ans = str(n1 + n2)[::-1]
        if ans == "0":
            head = ListNode(ans)
            return head

        dummy = ListNode(0)
        curr = dummy
        for i in ans:
                curr.next = ListNode(int(i))
                curr = curr.next
        return dummy.next
        
