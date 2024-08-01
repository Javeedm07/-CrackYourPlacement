class Solution:
    def divide(self, head):
        even = []
        odd = []
        ptr = head
        while ptr:
            if ptr.data % 2 == 0:
                even.append(ptr.data)
            else:
                odd.append(ptr.data)
            ptr = ptr.next
        ptr = head
        l = even + odd
        for i in l:
            ptr.data = i
            ptr = ptr.next
        return head
