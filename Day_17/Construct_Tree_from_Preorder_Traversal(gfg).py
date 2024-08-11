"""
Intuition:
This code constructs a binary tree from a preorder traversal (`pre`) and a leaf/non-leaf indicator array (`preLN`). It recursively builds the tree by popping elements 
from `pre` to create nodes, and using `preLN` to determine if a node is a leaf ('L') or non-leaf ('N'). For non-leaf nodes, the function recursively constructs the 
left and right subtrees.
"""

def solve(pre, preLN, n):
    if len(pre) == 0:
        return None
    root=Node(pre.pop(0))
    inst=preLN.pop(0)
    if inst=="L":
        return root
    else:
        root.left=constructTree(pre,preLN,n-1)
        root.right=constructTree(pre,preLN,n-1)
    return root

def constructTree(pre, preLN, n):
    return solve(pre, preLN, n)
