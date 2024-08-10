class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.count = 0
    
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.ans = root.val
                return
            inorder(root.right)

        inorder(root)
        return self.ans
