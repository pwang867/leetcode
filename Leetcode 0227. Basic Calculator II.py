"""
227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution:
    def calculate(self, s: str) -> int:
        ans, sign, x, op, y = 0, 1, 1, "*", 0
        for c in s:
            if c == " ":
                continue
            elif c == "+" or c == "-":
                if op == "*":
                    ans += sign * (x * y)
                else:
                    ans += sign * (x // y)
                sign, x, op, y = 1 if c == "+" else -1, 1, "*", 0
            elif c == "*" or c == "/":
                x = x * y if op == "*" else x // y
                y = 0
                op = c
            else:
                y = 10 * y + int(c)
        ans += sign * (x * y if op == "*" else x // y)
        return ans