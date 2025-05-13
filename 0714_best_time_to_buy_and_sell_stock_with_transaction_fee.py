# n = len(prices)
# Time: O(n)
# Space: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)

        return cash
