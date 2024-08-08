"""
Intuition:
This code checks whether two binary trees `p` and `q` are identical. It first verifies that both nodes are `None`, returning `True` if so. If one node is `None` and 
the other isn't, it returns `False`. If both nodes have the same value, the function recursively checks whether their left and right subtrees are also identical. The 
function returns `True` only if all corresponding nodes in both trees match.
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
