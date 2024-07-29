"""
Intuition:
The code checks if a singly linked list is a palindrome. It first traverses the list, storing each node's value in a list `l`. Then, it traverses the list again, 
comparing each node's value with the values popped from `l` (which are in reverse order). If all values match, it returns `True`, indicating the list is a palindrome; 
otherwise, it returns `False`.
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        ptr = head
        while ptr != None:
            l.append(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr != None:
            if ptr.val != l.pop():
                  return False
            ptr = ptr.next
        return True
