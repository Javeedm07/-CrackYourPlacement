"""
Intuition:
This code finds the intersection node of two singly linked lists. It first calculates the lengths of both lists, then aligns the starting points of the two lists 
by advancing the pointer of the longer list by the difference in lengths. It then simultaneously traverses both lists until it finds a common node, which it returns 
as the intersection node. If no intersection is found, it returns `None`.
"""
class Solution:
    def find_length(self, head):
        c = 0
        ptr = head
        while ptr != None:
            c += 1
            ptr = ptr.next
        return c

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = self.find_length(headA)
        n2 = self.find_length(headB)
        ptr1 = headA
        ptr2 = headB
        if n1 > n2:
            for i in range(n1 - n2):
                ptr1 = ptr1.next
        else:
            for i in range(n2 - n1):
                ptr2 = ptr2.next
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return ptr1
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        return None
      
"""
Intuition:
This code finds the intersection node of two singly linked lists. It uses two pointers, `a` and `b`, initialized to the heads of `headA` and `headB`, respectively. 
By alternating the traversal between the two lists when either pointer reaches the end, it ensures that both pointers traverse equal lengths, meeting at the 
intersection node or at `None` if there is no intersection. The loop continues until the pointers are equal, either at the intersection node or at the end of the 
lists (`None`).
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        a = headA
        b = headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a
