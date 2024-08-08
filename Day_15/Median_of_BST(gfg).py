"""
Intuition:
This code finds the median of a Binary Search Tree (BST). It first performs an in-order traversal to collect all node values in a sorted list (`result`). Since an 
in-order traversal of a BST produces a sorted sequence, the median can be easily found by accessing the middle element(s) of this list. If the list length is odd, 
the median is the middle element; if even, it's the average of the two middle elements.
"""

def findMedian(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.data)
        inorder(node.right)
        
    inorder(root)
    mid = len(result) // 2
    if len(result) % 2 == 1:
        return result[mid]
    else:
        ans = (result[mid] + result[mid - 1]) / 2
        if int(ans) == ans:
            return int(ans)
        else:
            return ans
