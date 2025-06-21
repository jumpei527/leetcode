# n = len(s)
# Time: O(n)
# Space: O(n)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []

        for char in s:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)

        return "".join(res)
