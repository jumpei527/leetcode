# n = len(pattern)
# Time: O(n)
# Space: O(n)


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pending_digits = []
        result = []
        for i in range(len(pattern) + 1):
            pending_digits.append(str(i+1))

            if i == len(pattern) or pattern[i] == "I":
                while pending_digits:
                    digit = pending_digits.pop()
                    result.append(digit)

        return "".join(result)
