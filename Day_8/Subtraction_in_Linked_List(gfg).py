"""
Intuition:
The code subtracts the numbers represented by two linked lists `l1` and `l2`. It converts the linked lists to their integer values (`n1` and `n2`) by traversing each 
list and forming the numbers. It then computes the absolute difference of these two numbers and converts the result back to a linked list format. The result is 
written back into the longer of the original linked lists (based on the larger number), effectively overwriting its nodes with the digits of the computed difference.
"""
class Solution:
    def subLinkedList(self, l1, l2): 
        ptr1 = l1
        ptr2 = l2
        n1 = 0
        n2 = 0
        while ptr1:
            n1 = n1* 10 + ptr1.data
            ptr1 = ptr1.next
        while ptr2:
            n2 = n2 * 10 + ptr2.data
            ptr2 = ptr2.next
        ans = str(abs(n1 - n2))
        ptr = l1 if n1 > n2 else l2
        temp = ptr
        x = Node(0)
        x.next = temp
        for i in ans:
            ptr.data = int(i)
            ptr = ptr.next
            x = x.next
        x.next = None
        return temp
