"""
Intuition:
This `intToRoman` function converts an integer `num` into its Roman numeral representation. It iterates over a list of Roman symbols and their corresponding values in
descending order. For each symbol, it determines how many times the symbol fits into `num` (using integer division) and appends the corresponding Roman numeral to the
result string `ans`, while reducing `num` by the symbol's value. The process continues until `num` is fully converted.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = [[1, 'I'], [4, 'IV'], [5, 'V'], [9, 'IX'], [10, 'X'], [40, 'XL'], [50, 'L'], [90, 'XC'], [100, 'C'], [400, 'CD'], [500, 'D'], [900, 'CM'], 
                  [1000, 'M']]
        ans = ""
        for i in range(len(symbol) - 1, -1, -1):
            if num // symbol[i][0]:
                count = num // symbol[i][0]
                ans += symbol[i][1] * count
                num = num % symbol[i][0]
        return ans
            
