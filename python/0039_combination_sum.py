# n = len(candidates)
# Time: O(n^target)
# Space: O(target)
from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        self.combinations_arr = []
        self.backtrack(candidates, [], target, 0)
        return self.combinations_arr

    def backtrack(
        self,
        candidates: List[int],
        combination: List[int],
        target: int,
        start: int
    ) -> None:
        if target == 0:
            self.combinations_arr.append(combination[:])
            return
        if target < 0:
            return

        for idx in range(start, len(candidates)):
            combination.append(candidates[idx])
            self.backtrack(
                candidates, combination, target - candidates[idx], idx
            )
            combination.pop()
