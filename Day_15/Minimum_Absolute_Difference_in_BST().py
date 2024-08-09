"""
Intuition:
This code finds the minimum absolute difference between values of any two nodes in a Binary Search Tree (BST). It first performs an in-order traversal to collect all 
node values in a sorted list `l`. Since the in-order traversal of a BST produces a sorted sequence, the code then iterates through the list, computing the differences 
between consecutive elements to find the smallest difference. This smallest difference is returned as the result.
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []

        def inorder(root):
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                l.append(root.val)
                root = root.right
    
        inorder(root)
        ans = sys.maxsize - 1
        for i in range(len(l) - 1):
            ans = min(ans, l[i + 1] - l[i])
        return ans
