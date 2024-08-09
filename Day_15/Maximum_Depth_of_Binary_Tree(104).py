"""
Intuition:
This code calculates the maximum depth (or height) of a binary tree. It does so recursively by checking if the current node is `None`; if so, it returns `0` as the 
depth. Otherwise, it recursively computes the maximum depth of the left and right subtrees (`ld` and `rd`), and then returns `1` plus the greater of the two depths. 
This ensures that the maximum depth from the root to the farthest leaf is correctly calculated.
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return 1 + max(ld, rd)
