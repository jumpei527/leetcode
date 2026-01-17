# n = len(digits)
# Time: O(n^4)
# Space: O(n)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.ans = []
        self.digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.backtrack(0, digits, "")

        return self.ans

    def backtrack(self, idx: int, digits: str, letters: str) -> None:
        if idx == len(digits):
            self.ans.append(letters)
            return
        for letter in self.digit_to_letters[digits[idx]]:
            self.backtrack(idx + 1, digits, letters + letter)
