"""
Intuition:
This code calculates the sum of all left leaves in a binary tree. The `dfs` (depth-first search) function traverses the tree. If a node has a left child that is a 
leaf (i.e., it has no children), its value is added to the cumulative sum `self.ans`. The function recursively explores both left and right subtrees. The total sum 
of left leaves is returned after the traversal is complete.
"""

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return
            if root.left and (not root.left.left and not root.left.right):
                self.ans += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans
