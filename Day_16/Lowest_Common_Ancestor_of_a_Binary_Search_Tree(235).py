"""
Intuition:
This code finds the lowest common ancestor (LCA) of two nodes (`p` and `q`) in a binary search tree (BST). It traverses the tree starting from the root, moving to the 
right if both nodes are greater than the current node, and to the left if both are smaller. The traversal stops when one node is on one side and the other node on the 
other side, or when one of the nodes matches the current node. This current node is returned as the LCA.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        temp = root 
        while temp:
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif p.val < temp.val and q.val < temp.val:
                temp = temp.left
            else:
                return temp
