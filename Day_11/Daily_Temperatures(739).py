"""
Intuition:
This code defines a method `dailyTemperatures` that calculates the number of days until a warmer temperature for each day in the input list `temperatures`. It uses 
a stack to keep track of indices of days with unresolved temperatures. As it iterates through the list, it updates the result list `res` with the difference in days 
when a warmer temperature is found, and then continues by pushing the current day's index onto the stack. The final result is a list of days until a warmer 
temperature for each day.
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
        return res
