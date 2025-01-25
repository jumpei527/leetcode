# n = len(tokens)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = []
        operator = {"+", "-", "*", "/"}

        for t in tokens:
            if t in operator:
                num1 = nums_stack.pop()
                num2 = nums_stack.pop()
                nums_stack.append(self.calculate(num1, num2, t))
            else:
                nums_stack.append(int(t))

        return nums_stack[0]

    def calculate(self, num1, num2, operator):
        if operator == "+":
            return num2 + num1
        if operator == "-":
            return num2 - num1
        if operator == "*":
            return num2 * num1
        if operator == "/":
            return int(num2 / num1)
