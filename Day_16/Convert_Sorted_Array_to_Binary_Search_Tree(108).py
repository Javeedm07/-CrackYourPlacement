"""
Intuition:
This code converts a sorted array into a height-balanced Binary Search Tree (BST). The `helper` function is a recursive function that selects the middle element of 
the current subarray as the root to ensure balance. It then recursively builds the left and right subtrees using the left and right halves of the array. The process 
continues until the entire array is converted into a balanced BST, and the root of this tree is returned.
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        return helper(0, len(nums) - 1)
