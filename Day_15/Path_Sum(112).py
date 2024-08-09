"""
Intuition:
This code checks if there is a root-to-leaf path in a binary tree where the sum of the node values equals a given `targetSum`. The `has_sum` function recursively 
traverses the tree, adding the current node's value to a running sum (`curr_sum`). If a leaf node is reached, it checks if the running sum equals `targetSum`. The 
function returns `True` if such a path exists, and `False` otherwise.
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, curr_sum):
            if not root:
                return False
            curr_sum += root.val
            if not root.left and not root.right:
                return curr_sum == targetSum
            return has_sum(root.left, curr_sum) or has_sum(root.right, curr_sum)
        
        return has_sum(root, 0)
