"""
Intuition:
This code generates all root-to-leaf paths in a binary tree as strings. The `path` function recursively traverses the tree, building a path string `s` by adding the 
current node's value. If a leaf node is reached (a node with no children), the complete path string is added to the `ans` list. The function continues to build the 
path strings for both left and right subtrees. Finally, the list `ans` containing all root-to-leaf paths is returned.
"""

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def path(root, s):
            if root:
                s += str(root.val)
                if not root.right and not root.left:
                    ans.append(s)
                else:
                    s += '->'
                    path(root.left, s)
                    path(root.right, s)
        
        path(root, "")
        return ans
