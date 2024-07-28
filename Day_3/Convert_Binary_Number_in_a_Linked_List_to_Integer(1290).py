"""
Intuition:
The code converts a binary number represented by a linked list into its decimal value. It constructs a binary string by traversing the linked list and 
concatenating each node's value, then converts this binary string to an integer using base 2.
"""

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        ptr = head
        while ptr != None:
            s += str(ptr.val)
            ptr = ptr.next
        return int(s, 2)
