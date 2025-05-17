# n = len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def removeStars(self, s: str) -> str:
        result_str = []

        for char in s:
            if char == "*":
                result_str.pop()
            else:
                result_str.append(char)

        return "".join(result_str)
