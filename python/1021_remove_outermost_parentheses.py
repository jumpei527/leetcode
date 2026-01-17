# n = len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        parentheses = []
        opened_count = 0

        for char in s:
            if char == "(" and opened_count > 0:
                parentheses.append(char)
            elif char == ")" and opened_count > 1:
                parentheses.append(char)
            opened_count += 1 if char == "(" else -1

        return "".join(parentheses)
