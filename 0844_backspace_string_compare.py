class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.apply_backspaces(s) == self.apply_backspaces(t)

    def apply_backspaces(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
