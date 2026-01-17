class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        prev_operator = "+"
        num = 0
        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in "+-*/" or idx == len(s)-1:
                if prev_operator == "+":
                    stack.append(num)
                elif prev_operator == "-":
                    stack.append(-num)
                elif prev_operator == "*":
                    stack.append(stack.pop() * num)
                elif prev_operator == "/":
                    stack.append(int(stack.pop() / num))

                prev_operator = char
                num = 0

        return sum(stack)
