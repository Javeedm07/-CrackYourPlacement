"""
Intuition:
The code reverses the input linked list to process nodes from the end to the beginning. It then traverses the reversed list, keeping track of the maximum value 
encountered. Nodes with values less than this maximum are removed. Finally, the list is reversed again to restore the original order with only the required nodes 
retained. This approach ensures the list is processed efficiently in a single traversal for filtering and another for restoration.
"""
class Solution:
    def reverse_list(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        
    def compute(self, head):
        head = self.reverse_list(head)
        max_val = head.data
        current = head
        while current and current.next:
            if current.next.data < max_val:
                current.next = current.next.next
            else:
                current = current.next
                max_val = current.data
        head = self.reverse_list(head)
        return head
