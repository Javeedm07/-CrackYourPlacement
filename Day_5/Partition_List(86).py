"""
Intuition:
The code partitions a linked list around a value x, such that all nodes with values less than x come before nodes with values greater than or equal to x. It first 
extracts all node values into a list, then separates this list into two parts: values less than x and values greater than or equal to x. These lists are 
concatenated, and the original linked list nodes are updated with the new order of values. The modified linked list is then returned.
"""

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        ptr = head
        while ptr:
            l.append(ptr.val)
            ptr = ptr.next
          
        ans1 = []
        ans2 = []
        for i in l:
            if i < x:
                ans1.append(i)
            else:
                ans2.append(i)
        ans1 = ans1 + ans2
      
        ptr = head
        for i in ans1:
            ptr.val = i
            ptr = ptr.next
        return head
