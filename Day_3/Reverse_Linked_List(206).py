"""
Approach - 1 : Using Stack
Intuition:
The code reverses a singly linked list using a stack. It first traverses the list, pushing each node's value onto the stack. Then, it traverses the list again,
popping values from the stack and updating each node's value with the popped value. This effectively reverses the list, and the modified list is returned.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head
        while ptr != None:
            stack.append(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr != None:
            ptr.val = stack.pop()
            ptr = ptr.next
        return head

"""
Approach - 2: Using 3 pointer approach
Intuition:
The code reverses a singly linked list in-place. It uses three pointers: `temp` to traverse the list, `prev` to keep track of the previous node, and `front` 
to temporarily store the next node. During each iteration, it reverses the current node's pointer to point to `prev`, then moves `prev` and `temp` one step 
forward. Finally, it returns `prev`, which becomes the new head of the reversed list.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
