"""
Intuition:
The code calculates the maximum profit from a single buy-sell transaction in a list of stock prices. It iterates through the list, updating the lowest buy price 
seen so far and calculating the potential profit at each step, keeping track of the maximum profit.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            profit = max(profit, p - buy_price)
        return profit
