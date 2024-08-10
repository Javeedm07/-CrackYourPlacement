"""
Intuition:
This code performs a level order traversal of a binary tree and returns a list of lists, where each inner list contains the values of nodes at that level. The `height`
function calculates the height of the tree to determine how many levels there are. The `helper` function recursively traverses the tree, adding each node's value to 
the corresponding level in the `ans` list. The `ans` list is initialized with empty sublists for each level, and the final result is returned.
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return 1 + max(lh, rh)

        def helper(node, level):
            if not node:
                return None
            ans[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)

        ans = [[] for _ in range(height(root))]
        helper(root, 0)
        return ans
