"""
Intuition:
The code multiplies two numbers represented by singly linked lists. The `list_to_number` method converts a linked list to an integer by traversing the list, 
updating `num` by shifting its digits left and adding the current node's value, while keeping it within a large number limit (`MOD`). The `multiply_two_lists` 
method uses this helper to convert both lists to numbers, multiplies these numbers, and returns the result modulo `10^9 + 7` to handle large outputs.
"""

MOD = 10**9+7
class Solution:
    def list_to_number(self, head):
        num = 0
        # MOD = 10**9 + 7
        current = head
        while current:
            num = (num * 10 + current.data) % MOD
            current = current.next
        return num
    
    def multiply_two_lists(self, head1, head2):
        # MOD = 10**9 + 7
        num1 = self.list_to_number(head1)
        num2 = self.list_to_number(head2)
        return (num1 * num2) % MOD
