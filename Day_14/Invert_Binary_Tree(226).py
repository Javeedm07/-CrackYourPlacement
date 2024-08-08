"""
Intuition:
The problem involves inverting a binary tree, which means swapping the left and right children of every node in the tree. The intuition is straightforward: for each 
node, you need to recursively swap its left and right subtrees until the entire tree is inverted.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
