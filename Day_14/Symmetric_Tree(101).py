"""
Intuition:
This code checks if a binary tree is symmetric, meaning it is a mirror image of itself. The `same` function compares two subtrees, ensuring they have the same 
structure and values in mirrored positions. It recursively checks if the left subtree of one side matches the right subtree of the other, and vice versa. The 
`isSymmetric` function initiates this check by comparing the tree with itself, returning `True` if the tree is symmetric and `False` otherwise.
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return same(root1.right, root2.left) and same(root1.left, root2.right)
            
        return same(root, root)
