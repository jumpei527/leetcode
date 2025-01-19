# n = len(tokens)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = []

        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                self.calculate(nums_stack, t)
            else:
                nums_stack.append(int(t))

        return nums_stack[0]

    def calculate(self, nums_stack, token):
        num1 = nums_stack.pop()
        num2 = nums_stack.pop()
        if token == "+":
            nums_stack.append(num2 + num1)
        if token == "-":
            nums_stack.append(num2 - num1)
        if token == "*":
            nums_stack.append(num2 * num1)
        if token == "/":
            nums_stack.append(int(num2 / num1))
