"""
Intuition:
This code checks if a binary tree is a valid Binary Search Tree (BST). The `helper` function recursively validates each node by ensuring that its value lies within a 
specified range (`left` and `right`). For each node, the left subtree is checked with an updated upper bound (the current node's value), and the right subtree is 
checked with an updated lower bound. If all nodes satisfy the BST property, the function returns `True`; otherwise, it returns `False`.
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, left, right):
            if not root:
                return True
            if not(left < root.val < right):
                return False
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        return helper(root, float('-inf'), float('inf'))
