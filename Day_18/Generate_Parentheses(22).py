"""
Intuition:
The `generateParenthesis` function generates all valid combinations of `n` pairs of parentheses. It uses a recursive backtracking approach, where `open` tracks the 
number of open parentheses and `close` tracks the number of close parentheses in the current string `s`. The function ensures that no more closing parentheses are 
added than opening ones, and adds a valid combination to the result list `ans` once `open` and `close` both reach `n`.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(open, close, s):
            if open == close and open + close == 2 * n:
                ans.append(''.join(s))
                return
            if open < n:
                backtrack(open + 1, close, s + '(')
            if open > close:
                backtrack(open, close + 1, s + ')')

        backtrack(0, 0, "")
        return ans
