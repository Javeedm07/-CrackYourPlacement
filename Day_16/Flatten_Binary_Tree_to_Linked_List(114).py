"""
Intuition:
This code flattens a binary tree into a linked list following a pre-order traversal. First, the `preorder` function collects all the node values in the order they are 
visited. Then, starting from the root, the code reconstructs the tree by setting each node's left child to `None` and its right child to the next node in the collected 
list, effectively converting the tree into a single right-skewed linked list.
"""

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        #Don't return anything. Just modify the root node
        self.ans = []
        
        def preorder(node):
            if not node:
                return None
            self.ans.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        
        curr = root
        for i in self.ans[1 : ]:
            curr.left = None
            curr.right = TreeNode(i)
            curr = curr.right
