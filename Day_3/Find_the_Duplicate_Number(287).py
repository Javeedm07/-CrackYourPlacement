"""
Intuition:
It first identifies a cycle by advancing two pointers at different speeds: slow moves one step at a time and fast moves two steps at a time. Once they meet, it confirms a cycle. To find the entry point of 
the cycle (the duplicate number), it resets one pointer to the start and advances both pointers one step at a time until they meet again, which is the duplicate number.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Using Hare and Tortoise method
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow

"""
Intuition:
The code finds a duplicate number in a list by using a set to track seen numbers. It iterates through the list, and if a number is already in the set, it returns that number as the duplicate. 
If not, it adds the number to the set and continues.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      #Using set
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
