"""
Intuition:
This code calculates the maximum width of a binary tree. The `helper` function traverses the tree in a level-order fashion, storing the positions of nodes at each 
level. The width at each level is determined by the difference between the first and last node positions. The maximum width across all levels is then returned as 
the result. If the tree is empty, it returns `0`.
"""

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        def helper(node, level, pos):
            if not node:
                return
            if len(ans) == level:
                ans.append([pos])
            else:
                ans[level].append(pos)
            
            helper(node.left, level + 1, 2 * pos + 1)
            helper(node.right, level + 1, 2 * pos + 2)

        ans = []
        helper(root, 0, 0)
        max_width = 1
        for level in ans:
            if len(level) > 1:
                max_width = max(max_width, level[-1] - level[0] + 1)
        return max_width
