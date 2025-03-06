# Time: (n*k)
# Space: (k)
from typing import List


class Solution:
    def combine(
        self, n: int, k: int
    ) -> List[List[int]]:
        self.combinations = []
        self.backtrack(1, [], n, k)

        return self.combinations

    def backtrack(
        self, start: int, combination: List[int], n: int, k: int
    ) -> None:
        if len(combination) == k:
            self.combinations.append(combination[:])
            return

        for num in range(start, n + 1):
            combination.append(num)
            self.backtrack(num + 1, combination, n, k)
            combination.pop()
