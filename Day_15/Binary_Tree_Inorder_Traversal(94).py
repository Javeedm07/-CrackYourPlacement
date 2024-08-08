"""
Intuition:
This code performs an in-order traversal of a Binary Search Tree (BST) iteratively using a stack. The algorithm pushes nodes onto the stack as it traverses the left 
subtree. Once it reaches a leaf (leftmost node), it starts popping nodes from the stack, adding their values to the result list, and then traverses the right subtree. 
This ensures that nodes are processed in ascending order, reflecting the in-order traversal of the BST.
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
