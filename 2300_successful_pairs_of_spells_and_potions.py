# n = len(spells)
# m = len(potions)
# Time: O(n log m)
# Space: O(m)
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        ans = []
        potions.sort()
        potions_num = len(potions)
        for spell in spells:
            success_idx = self.binary_search(spell, potions, success)
            ans.append(potions_num - success_idx)

        return ans

    def binary_search(
        self, spell: int, potions: List[int], success: int
    ) -> int:
        left = -1
        right = len(potions)
        while right - left > 1:
            mid = (left + right) // 2
            if potions[mid] * spell < success:
                left = mid
            else:
                right = mid

        return right
