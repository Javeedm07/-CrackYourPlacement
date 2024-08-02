"""
Intuition:
The code defines a function `topKFrequent` that finds the `k` most frequent elements in a list `nums`. It first counts the frequency of each element using `Counter`. 
Then, it uses a max-heap (simulated with negative counts) to store the frequencies and their corresponding elements. Finally, it extracts the top `k` elements with the 
highest frequencies from the heap and returns them.
"""

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for i, j in counter.items():
            heapq.heappush(heap, (-j, i))
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(heap)[1])
        return ans
