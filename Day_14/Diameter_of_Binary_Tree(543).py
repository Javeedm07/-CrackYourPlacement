"""
Intuition:
This code defines a function `diameterOfBinaryTree` that calculates the diameter of a binary tree, where the diameter is the longest path between any two nodes. The 
`height` helper function recursively calculates the height of the tree and updates the `ans` list with the maximum diameter found. The diameter at any node is the sum 
of the heights of its left and right subtrees. The function returns the maximum diameter found during the traversal.
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def height(root):
            if root == None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            diameter = lh + rh
            ans[0] = max(ans[0], diameter)
            return 1 + max(lh, rh)

        height(root)
        return ans[0]
