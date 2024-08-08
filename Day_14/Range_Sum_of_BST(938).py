"""
Intuition:
This code calculates the sum of all node values within a specified range `[low, high]` in a Binary Search Tree (BST). It recursively traverses the tree, skipping the 
left subtree if the current node's value is less than `low` and skipping the right subtree if the value is greater than `high`. If the node's value is within the 
range, it adds the value to the sum and continues searching both subtrees. The function returns the total sum of values within the range.
"""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
