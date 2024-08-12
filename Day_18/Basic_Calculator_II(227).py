"""
Intuition:
The `calculate` function evaluates a basic arithmetic expression containing integers and the operators `+`, `-`, `*`, and `/`. It uses a stack to handle operator 
precedence, building numbers from digits, and performing operations based on the previous operator. By iterating through the expression and updating the stack 
accordingly, it computes the final result by summing the values in the stack.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, op = [], 0, '+'
        for c in s + '+':
            if c == " ":
                continue
            elif c.isdigit():
                cur = (cur * 10) + int(c)
            else:
                if op == '-':
                    stack.append(-cur)
                elif op == '+':
                    stack.append(cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                elif op == '/':
                    stack.append(int(stack.pop() / cur))
                cur, op = 0, c
        return sum(stack)
