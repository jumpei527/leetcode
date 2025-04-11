# n = len(columnTitle)
# Time: O(n)
# Space: O(1)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0

        for idx in range(len(columnTitle)):
            columnNumber *= 26
            columnNumber += ord(columnTitle[idx]) - ord("A") + 1

        return columnNumber
