"""
Intuition:
This code finds the size of the largest Binary Search Tree (BST) within a given binary tree. The `isBst` method checks whether a subtree is a valid BST by ensuring 
all nodes' values fall within a valid range (`low < root.data < high`). The `num_of_Nodes` method counts the total nodes in a subtree. The `largestBst` method 
recursively checks each subtree, and if a subtree is a valid BST, it updates the maximum size (`self.ans`) with the number of nodes in that subtree. Finally, it 
returns the size of the largest BST found.
"""

class Solution:
    def __init__(self):
        self.ans = 0
        
    def isBst(self, root, low, high):
        if not root:
            return True
        if not(low < root.data < high):
            return False
        return self.isBst(root.left, low, root.data) and self.isBst(root.right, root.data, high)
    
    def num_of_Nodes(self, root):
        if not root:
            return 0
        return 1 + self.num_of_Nodes(root.left) + self.num_of_Nodes(root.right)

    def largestBst(self, root):
        if not root:
            return 0
        if self.isBst(root, float('-inf'), float('inf')):
            n = self.num_of_Nodes(root)
            self.ans = max(self.ans, n)
        if root.left:
            self.largestBst(root.left)
        if root.right:
            self.largestBst(root.right)
        return self.ans
