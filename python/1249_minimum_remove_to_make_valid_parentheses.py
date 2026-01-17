# n = len(s)
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[idx] = ""

        while stack:
            s_list[stack.pop()] = ""

        return "".join(s_list)
