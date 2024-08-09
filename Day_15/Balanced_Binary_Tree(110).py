"""
Intuition:
This code checks if a binary tree is balanced by using a recursive approach. The `height` function calculates the height of the tree while also checking for balance. 
If any subtree is unbalanced (i.e., the height difference between left and right subtrees is greater than 1), the function returns `-1`. If the tree is balanced, it 
returns the actual height. The `isBalanced` function returns `True` if the tree is balanced (i.e., the height is non-negative) and `False` otherwise.
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    
    def height(self, root):
        if not root:
            return 0
        lh, rh = self.height(root.left), self.height(root.right)
        if lh < 0 or rh < 0 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)
