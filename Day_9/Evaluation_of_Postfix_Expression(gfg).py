"""
Intuition:
This code defines a class `Solution` with a method `evaluatePostfix` that evaluates a postfix expression given as a string `S`. It uses a stack to process the 
expression: operands are pushed onto the stack, and operators pop the required operands from the stack, perform the operation, and push the result back. The final 
result is the last remaining element in the stack.
"""

class Solution:
    def evaluatePostfix(self, S):
        stack = []
        operators = ['+', '-', '*', '/']
        for i in S:
            if i in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                if i == '+':
                    ans = (n2 + n1)
                elif i == '-':
                    ans = (n2 - n1)
                elif i == '*':
                    ans = (n2 * n1)
                else:
                    ans = (n2 // n1)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[0]
