"""
Intuition:
The code defines a function `findKthLargest` that finds the k-th largest element in a list `nums`. It starts by creating a min-heap from the first `k` elements of 
`nums`. Then, for each remaining element in `nums`, if the element is larger than the smallest element in the heap (the heap root), it replaces the heap root with 
the new element. This ensures that the heap always contains the k largest elements, and the k-th largest element will be at the root of the heap.
"""

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[ : k]
        heapq.heapify(heap)
        for i in nums[k : ]:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]
