"""
Intuition:
The code merges two sorted singly linked lists into one sorted list. It uses a dummy node to simplify the merging process and a `curr` pointer to build the new list. 
It iterates through both lists, appending the smaller node to `curr.next` and moving the pointer of the appended list forward. Once one list is exhausted, it appends 
the remaining nodes of the other list. Finally, it returns the merged list starting from `dummy.next`.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            return dummy.next
