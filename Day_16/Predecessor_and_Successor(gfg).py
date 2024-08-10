"""
Intuition:
This code finds the predecessor (`pre`) and successor (`suc`) of a given key in a binary search tree (BST). It does so by performing an inorder traversal of the 
BST, which visits nodes in ascending order and stores their values in a list (`nodes`). After the traversal, it searches the list for the position of the given 
key and assigns the predecessor and successor based on neighboring values in the list. If no predecessor or successor exists, it sets them to `None`.
"""

class Solution:
    def findPreSuc(self, root, pre, suc, key):
        # Your code goes here
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            nodes.append(node.key)
            inorder(node.right)
        
        nodes = []
        inorder(root)
        i = 0
        while i < len(nodes):
            if nodes[i] < key:
                i += 1
            else:
                break
        if i > 0:
            pre.key = nodes[i - 1]   
        if i < len(nodes):
            if nodes[i] > key:
                suc.key = nodes[i]
            else:
                suc.key = nodes[i + 1] if i < len(nodes) - 1 else None
