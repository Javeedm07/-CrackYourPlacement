"""
Intuition:
This code generates the right side view of a binary tree, which is the set of nodes visible when the tree is viewed from the right side. It uses a depth-first search
(DFS) approach, where it traverses the tree level by level, prioritizing the right child before the left. If a node is the first one encountered at a particular level,
it is added to the result list (`ans`). The final list contains the values of nodes that make up the right side view of the tree.
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, level):
            if not node:
                return None 
            if len(ans) == level:
                ans.append(node.val)
            helper(node.right, level + 1)
            helper(node.left, level + 1)
        ans = []
        helper(root, 0)
        return ans
