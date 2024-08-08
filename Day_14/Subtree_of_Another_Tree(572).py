"""
Intuition:
This code checks if a binary tree `subRoot` is a subtree of another binary tree `root`. The `check` function recursively compares the nodes of `root` and `subRoot` 
to see if they are identical. The `has_subTree` function traverses the entire `root` tree, using `check` to determine if the current subtree matches `subRoot`. 
If a match is found, it returns `True`; otherwise, it continues checking the left and right subtrees. The main function returns whether `subRoot` is found as 
a subtree of `root`.
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(r, sr):
            if not r and not sr:
                return True
            if (r and not sr) or (not r and sr):
                return False
            if r.val != sr.val:
                return False
            return check(r.left, sr.left) and check(r.right, sr.right)
        
        def has_subTree(root):
            if root == None:
                return root
            if check(root, subRoot):
                return True
            return has_subTree(root.left) or has_subTree(root.right)

        return has_subTree(root)
