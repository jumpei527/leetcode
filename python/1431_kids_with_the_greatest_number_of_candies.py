# n = len(candies)
# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        result = []
        max_candy = max(candies)

        for candy in candies:
            is_max = (candy + extraCandies) >= max_candy
            result.append(is_max)

        return result
