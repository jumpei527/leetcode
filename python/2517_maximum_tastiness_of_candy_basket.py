# n = len(price)
# Time: O(nlogn)
# Space: O(1)
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left = 0
        right = price[-1] - price[0] + 1

        while right - left > 1:
            mid = (left + right) // 2
            if self.can_place_items(price, k, mid):
                left = mid
            else:
                right = mid

        return left

    def can_place_items(
        self, price: List[int], num_items: int, min_tastiness: int
    ) -> bool:
        count = 1
        last_price = price[0]

        for idx in range(1, len(price)):
            if price[idx] - last_price >= min_tastiness:
                count += 1
                if count >= num_items:
                    return True
                last_price = price[idx]

        return count >= num_items
