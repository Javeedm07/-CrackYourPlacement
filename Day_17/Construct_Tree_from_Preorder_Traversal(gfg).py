"""
Intuition:
This code constructs a binary tree from preorder traversal (`pre`) and a leaf/non-leaf indicator array (`preLN`). It creates a root node using the first element of 
`pre`, and checks if the node is a leaf ('L') or non-leaf ('N') using `preLN`. If it's a non-leaf, the function recursively constructs its left and right subtrees. 
If it's a leaf, it simply returns the node.
"""

def constructTree(pre, preLN, n):
    if len(pre) == 0:
        return None
    root=Node(pre.pop(0))
    inst=preLN.pop(0)
    if inst=="L":
        return root
    else:
        root.left= constructTree(pre,preLN, n-1)
        root.right= constructTree(pre,preLN, n-1)
    return root
