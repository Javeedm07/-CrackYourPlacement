"""
Intuition:
This code merges two binary trees by summing their corresponding nodes. The `dfs` function recursively traverses both trees, creating a new tree where each node's 
value is the sum of the values from `root1` and `root2`. If both nodes exist, their values are added; if only one exists, that node is used in the new tree. The 
function returns the merged tree rooted at the combined nodes, or the non-null node if only one is present.
"""

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1 and root2:
                root = TreeNode(root1.val + root2.val)
                root.left = dfs(root1.left, root2.left)
                root.right = dfs(root1.right, root2.right)
                return root
            else:
                return root1 or root2
        return dfs(root1, root2)
