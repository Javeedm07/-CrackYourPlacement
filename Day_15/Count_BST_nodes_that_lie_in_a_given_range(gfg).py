"""
Intuition:
This code counts the number of nodes in a Binary Search Tree (BST) that have values within a specified range `[low, high]`. It recursively traverses the tree, skipping 
the left subtree if the current node's value is less than `low` and skipping the right subtree if the value is greater than `high`. If the node's value is within the 
range, it increments the count and continues checking both subtrees. The total count of nodes within the range is returned.
"""

class Solution:
    def getCount(self,root,low,high):
        ##Your code here
        if not root:
            return 0
        if root.data < low:
            return self.getCount(root.right, low, high)
        elif root.data > high:
            return self.getCount(root.left, low, high)
        return 1 + self.getCount(root.right, low, high) + self.getCount(root.left, low, high)
