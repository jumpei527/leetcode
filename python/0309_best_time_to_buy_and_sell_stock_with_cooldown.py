# n = len(prices)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -float("inf")
        sold = 0
        rest = 0

        for idx in range(len(prices)):
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - prices[idx])
            sold = prev_hold + prices[idx]
            rest = max(prev_sold, prev_rest)

        return max(sold, rest)
