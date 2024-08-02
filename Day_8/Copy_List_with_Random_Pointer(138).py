"""
Intuition:
The code deep copies a linked list with `next` and `random` pointers. First, it creates new nodes and maps each original node to its copy using a hashmap. Then, it 
traverses the original list again to set the `next` and `random` pointers of the new nodes by looking up the corresponding nodes in the hashmap. Finally, it returns 
the head of the copied list.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        hmap = {}
        while curr != None:
            node = Node(x = curr.val)
            hmap[curr] = node
            curr = curr.next
        curr = head
        while curr != None:
            new_node = hmap[curr]
            new_node.next = hmap[curr.next] if curr.next else None
            new_node.random = hmap[curr.random] if curr.random else None
            curr = curr.next
        return hmap[head]
